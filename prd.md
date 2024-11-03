# Drafts to Markdown Converter

## Overview
A tool to convert JSON drafts into Markdown files with metadata and AI-generated titles.

## Features
1. JSON File Processing
   - Open and read JSON file containing draft entries
   - Parse JSON data structure
   - Handle multiple entries

2. Metadata Generation
   - Extract datetime information
   - Include creation/modification dates
   - Add other relevant metadata fields

3. AI Title Generation
   - Integrate with OpenAI API
   - Generate relevant titles based on content
   - Fallback handling if API fails

4. File Management
   - Create filename format: `YYMMDD title.md`
   - Handle file naming conflicts
   - Organize files in appropriate directory structure

## Technical Requirements

### Input
- JSON file containing draft entries
- Each entry must include:
  - Content
  - DateTime
  - Other metadata fields

### Processing
1. Read JSON file
2. For each entry:
   - Parse JSON data
   - Generate title using OpenAI
   - Format metadata
   - Create markdown content
   - Generate filename

### Output
- Markdown files with:
  - YAML frontmatter containing metadata
  - AI-generated title
  - Original content
  - Formatted datetime

## Implementation Steps
1. Setup JSON file reader
2. Implement JSON parser
3. Configure OpenAI integration
4. Create metadata formatter
5. Build markdown converter
6. Implement file writer
7. Add error handling

## Dependencies
- JSON processing library
- OpenAI API
- File system operations
- DateTime handling

## Success Criteria
- Successfully converts JSON to markdown
- Generates meaningful titles
- Maintains all metadata
- Creates properly formatted files
- Handles errors gracefully
