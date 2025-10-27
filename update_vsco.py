#!/usr/bin/env python3
"""
Update VSCO photos for the website.

AUTOMATED UPDATE (may not work reliably):
    python3 update_vsco.py

MANUAL UPDATE (recommended):
VSCO uses JavaScript to load images, so automated scraping is unreliable.
To manually update your photos:

1. Visit https://vsco.co/lostmonster/gallery
2. Open your browser's developer tools (F12)
3. Go to the Network tab and filter for "im.vsco.co"
4. Reload the page
5. Look for the image URLs that appear as you scroll
6. For each photo, copy the image URL and the media ID from the URL
7. Edit _data/vsco.json and add the new photos:

   {
     "url": "https://im.vsco.co/aws-us-west-2/2e57cf/296724/{MEDIA_ID}/{filename}.jpg",
     "permalink": "https://vsco.co/lostmonster/media/{MEDIA_ID}"
   }

8. Keep only the 6 most recent photos
9. Test locally and commit/push your changes
"""

import subprocess
import json
import re

def fetch_vsco_data():
    """Fetch recent photos from VSCO profile and save to _data/vsco.json"""
    
    print("Fetching VSCO profile data...")
    
    try:
        # Fetch the VSCO gallery page
        result = subprocess.run(
            ['curl', '-s', 'https://vsco.co/lostmonster/gallery'],
            capture_output=True,
            text=True
        )
        
        html_content = result.stdout
        
        # Extract all image URLs matching the VSCO CDN pattern
        # Pattern: https://im.vsco.co/aws-us-west-2/{site}/{userId}/{mediaId}/{filename}
        image_url_pattern = r'https://im\.vsco\.co/aws-us-west-2/[^/]+/[^/]+/([a-f0-9]+)/[^?"\s]+'
        all_urls = re.findall(image_url_pattern, html_content)
        
        # Extract URLs and their media IDs
        photos = []
        seen_ids = set()
        
        for match in re.finditer(image_url_pattern, html_content):
            url = match.group(0)
            media_id = match.group(1)
            
            # Only add if we haven't seen this media ID yet
            if media_id not in seen_ids and media_id:
                # Remove query parameters from URL for cleaner images
                clean_url = url.split('?')[0]
                permalink = f'https://vsco.co/lostmonster/media/{media_id}'
                
                photos.append({
                    'url': clean_url,
                    'permalink': permalink
                })
                seen_ids.add(media_id)
                
                if len(photos) >= 6:
                    break
        
        if photos:
            # Save to _data/vsco.json
            output_file = '_data/vsco.json'
            with open(output_file, 'w') as f:
                json.dump(photos, f, indent=2)
            
            print(f"✓ Successfully fetched {len(photos)} photos")
            print(f"✓ Saved to {output_file}")
            return True
        else:
            print("✗ Could not find photo data in VSCO HTML")
            print("Note: VSCO may use different HTML structure now")
            print("\nManual update instructions:")
            print("1. Visit https://vsco.co/lostmonster/gallery")
            print("2. Inspect page source to find image URLs")
            print("3. Update _data/vsco.json with new photos")
            return False
    
    except Exception as e:
        print(f"✗ Error: {e}")
        print("\nManual update instructions:")
        print("1. Visit https://vsco.co/lostmonster/gallery")
        print("2. Inspect page source to find image URLs")
        print("3. Update _data/vsco.json with new photos")
        return False

if __name__ == '__main__':
    success = fetch_vsco_data()
    if success:
        print("\nNext step: Commit and push your changes to update the live site")
    else:
        print("\nYou may need to manually update _data/vsco.json")

