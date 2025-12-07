
const Tesseract = require('tesseract.js');
const fs = require('fs');
const path = require('path');

const imagesDir = path.join(__dirname, 'public', 'slides_images');
const outputDir = path.join(__dirname, '.gemini', 'antigravity', 'brain', '06437ca2-2952-4d08-8897-581904284a54');
const outputFile = path.join(outputDir, 'extracted_slides.md');

// Ensure output directory exists (though it should)
if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir, { recursive: true });
}

async function extractText() {
    try {
        const files = fs.readdirSync(imagesDir).filter(file => file.endsWith('.png')).sort();
        let markdownContent = '';

        console.log(`Found ${files.length} images.`);

        for (const file of files) {
            console.log(`Processing ${file}...`);
            const filePath = path.join(imagesDir, file);

            const { data: { text } } = await Tesseract.recognize(
                filePath,
                'eng',
                { logger: m => console.log(m) }
            );

            markdownContent += `---
layout: default
---

# Slide extracted from ${file}

${text}

`;
        }

        fs.writeFileSync(outputFile, markdownContent);
        console.log(`Extraction complete. Saved to ${outputFile}`);
    } catch (error) {
        console.error('Error extracting text:', error);
    }
}

extractText();
