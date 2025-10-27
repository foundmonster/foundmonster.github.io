# VSCO Photo Section Update Instructions

## Overview
Your site displays the 6 most recent photos from your VSCO profile (https://vsco.co/lostmonster/gallery) in a masonry layout below the music section on the homepage.

## Files Involved
- **Data file:** `_data/vsco.json` - Contains the photo URLs and permalinks
- **Display:** The photos appear on `index.html` in the "Recent Photos" section
- **Styling:** CSS masonry layout in `_sass/main.scss` (`.photo-grid-masonry`)

## How to Update

### Step 1: Get the Latest Photos from VSCO
1. Visit https://vsco.co/lostmonster/gallery
2. Open your browser's developer tools (F12 or right-click → Inspect)
3. Go to the **Network** tab
4. Filter for "im.vsco.co" 
5. Reload the page (Cmd+R or F5)
6. Scroll down to load more photos
7. Look for image requests - they will appear as you scroll

### Step 2: Extract Photo Information
For each photo you want to add, you need:

**Example from the network logs:**
```
https://im.vsco.co/aws-us-west-2/2e57cf/296724/665b95a18e54a4062f5d3c0c/vsco_060124.jpg
```

**Extract the following:**
- **URL:** The full image URL (copy the whole thing)
- **Media ID:** The hex string (e.g., `665b95a18e54a4062f5d3c0c`)
- **Permalink:** Construct as `https://vsco.co/lostmonster/media/{MEDIA_ID}`

### Step 3: Update `_data/vsco.json`
Edit the file and update it with the structure:

```json
[
  {
    "url": "https://im.vsco.co/aws-us-west-2/2e57cf/296724/665b95a18e54a4062f5d3c0c/vsco_060124.jpg",
    "permalink": "https://vsco.co/lostmonster/media/665b95a18e54a4062f5d3c0c"
  },
  {
    "url": "https://im.vsco.co/aws-us-west-2/2e57cf/296724/665b95978e54a4062f5d3c0b/vsco_060124.jpg",
    "permalink": "https://vsco.co/lostmonster/media/665b95978e54a4062f5d3c0b"
  }
]
```

**Important:**
- Keep only the 6 most recent photos
- The most recent photo should be first in the array
- Make sure all URLs are valid and the JSON is properly formatted

### Step 4: Test and Deploy
1. The Jekyll server should auto-reload (check http://localhost:4000)
2. Verify the photos appear correctly
3. Commit and push your changes

## Quick Reference

**Pattern for VSCO image URLs:**
```
https://im.vsco.co/aws-us-west-2/2e57cf/296724/{MEDIA_ID}/{filename}.jpg
```

**Pattern for permalinks:**
```
https://vsco.co/lostmonster/media/{MEDIA_ID}
```

**Where the media ID appears in the URL:**
```
https://im.vsco.co/aws-us-west-2/2e57cf/296724/665b95a18e54a4062f5d3c0c/filename.jpg
                                    ↑ this is the MEDIA_ID ↑
```

## Alternative: Use Browser Console (Easier Method)
1. Visit https://vsco.co/lostmonster/gallery
2. Open browser console (F12 → Console tab)
3. Run this JavaScript code:

```javascript
// This will extract photo data from the page
const photos = [];
document.querySelectorAll('img').forEach(img => {
  const src = img.src;
  const dataId = img.getAttribute('data-id') || img.closest('[data-id]')?.getAttribute('data-id');
  if (src && src.includes('im.vsco.co')) {
    // Extract media ID from URL
    const match = src.match(/\/([a-f0-9]+)\/[^?"]+$/);
    if (match && match[1]) {
      const mediaId = match[1];
      photos.push({
        url: src.split('?')[0], // Remove query params
        permalink: `https://vsco.co/lostmonster/media/${mediaId}`
      });
    }
  }
});
// Copy the output
console.log(JSON.stringify(photos, null, 2));
```

4. Copy the output and paste into `_data/vsco.json`

## Why Not Automated?
VSCO uses JavaScript to lazy-load images, so the initial HTML doesn't contain all photo URLs. Manual extraction or browser console methods are more reliable.

