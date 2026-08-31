# Content Staging Folder

## Purpose
This folder is for **draft blog articles in Word format** before they're converted to published blog posts.

## Workflow

### 1. Create Your Article in Word
Write your content using standard Word features:

#### **Headings**
- **Heading 1**: Not used (reserved for article title)
- **Heading 2**: Main sections (will appear in table of contents)
- **Heading 3**: Subsections
- **Heading 4**: Sub-subsections

#### **Tables**
- Create tables directly in Word
- Your table structure will be preserved exactly
- Agent ensures consistent styling across all posts

#### **Images**
- **Option 1**: Insert image with caption
- **Option 2**: Add placeholder text like: `[Image: filename.jpg] Caption text here`
- Save actual image files to: `/images/journal/[post-slug]/filename.jpg`
- Agent will convert to proper markdown format and path

#### **Pull Quotes & Callouts**
- **Pull Quote**: Use Word's "Quote" style or indent + italics
- **Tip/Note Box**: Add marker like `[TIP]` or `[NOTE]` before the text
- **Highlight Box**: Use Word's text box or add `[HIGHLIGHT]` marker
- Agent will convert these to styled blockquotes with consistent formatting

#### **Lists**
- Bullet lists, numbered lists, and checklists are all supported
- Use Word's standard list formatting
- For checklists, use ☐ or ✓ characters

#### **Emphasis**
- **Bold** for emphasis
- *Italic* for subtle emphasis or quotes
- These convert directly to markdown

#### **Links**
- Use Word's hyperlink feature (Ctrl+K)
- Links will be properly styled in green with underline

### 2. Add Your Document Here
- Drop your Word document (.docx) in this folder
- Use any filename - it will be converted to the proper Jekyll format
- Example: `Journey Guide - Ayodhya and Varanasi - V2.docx`

### 3. Request Conversion
Tell the agent: "I've added/updated [article name], please convert to blog post"

### 4. Agent Processing
The agent will:
- **Respect your editorial decisions**: Tables, image placement, pull quotes, and structure stay exactly as you created them
- **Convert to markdown**: Clean, proper markdown syntax
- **Add technical elements**: Front matter (title, date, excerpt, featured image, permalink)
- **Apply consistent styling**: Site-wide fonts, colors, spacing, responsive design
- **Save as Jekyll post**: `_posts/YYYY-MM-DD-article-title.md`

### 5. What the Agent Does NOT Change
- Your content structure and hierarchy
- Table layouts you created
- Image placement decisions
- What you chose to emphasize (quotes, callouts, lists)
- Order of sections

### 6. What the Agent DOES Ensure
- Proper markdown syntax
- Consistent CSS styling across all posts
- Responsive design for mobile/tablet
- Table of contents generation (from H2 headings)
- Proper image paths and organization
- Link styling
- Section separators

### 7. After Publishing
- The Word doc stays here as your source of truth
- Update the Word doc for content changes
- Re-run conversion to update the published post
- This folder is excluded from Jekyll build - Word docs won't appear on site

## Notes
- This folder is excluded from the Jekyll build process
- **Images**: Each blog post has its own subfolder in `/images/journal/[post-slug]/`
  - Example: `/images/journal/ayodhya-varanasi-guide/` for the Ayodhya & Varanasi guide
  - This keeps images organized and prevents naming conflicts
- **Post slug**: Will be auto-generated from your article title
  - Example: "The Complete Guide to Ayodhya & Varanasi" → `ayodhya-varanasi-guide`
- **You control content**, agent handles technical consistency
