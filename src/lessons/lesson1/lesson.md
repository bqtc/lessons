# Existing Sites
## Open twitter.com (or facebook.com for better mobile representation)
### Discuss browser location / URL
* General structure: scheme, hostname, path, fragment/query
### Discuss visual elements
* General layout, boxes, and columns
* Some elements are (selectable) text, others are images, still others are "controls"
* Try selecting text on the page, note how the selection highlight flows across the page
* Note some control interactions (like form validation) occur on "events" (user input)
### Open the web inspector
* Note that webpages have three major components: structure (HTML), style (CSS), and behavior (Javascript)
* All three are described textually
* Handle assets/resources (like images) later
### Switch to elements inspector
* Note that HTML is described with "tags" using angle brackets (&lt;&gt;), and have "open" and "close" types
* Note the general code coloring, and start selecting elements to indicate their position on the page (side-by-side)
* This demonstrates the relationship between the (still) incomprehensible text and its visual representation
### Pick a simple tag (H2 or P)
* Explain how structure/content is contained between the tags, and attributes are provided in the open tag
* Examine some of the tag's characteristics: tag style, classes, inline style, and contents
* Briefly discuss style, and its difference between structure/content
### Select other tags
* Note how sibling elements may be laid out nonlinearly
* Brief discussion of the semantic web? Different tags have different meanings/uses/purposes, more like a report written in Microsoft Word
### Switch to [Re]sources Inspector
* Discuss other assets used by the page, like images and javascript
* All are referenced (at root) by the HTML file which is the page
### Try submitting a form
* Even empty, the URL may change, and content returned will be based on form contents
# Modifying Content
## Existing Site
### Picking
* Ask the student to choose a textual element on the page using the Element Inspector
* This may require fine-grained control over the exact element, if several overlap
* In the Inspector, double-click the selected tag to begin editing
### Editing
* Ask the student to type in the text of their choice
### Committing
* Press Enter/Return to commit the changes
* Observe the results in the live view
### More Exercise
* Edit several elements on the page in the same way, noting cases where larger replacements may "break" the style
* Try emptying a tag's contents to observe the change to layout
* Point out cases where the visual element may be an image rather than text
# Modifying Style
## Existing Site
### Picking
* Refresh the page to clear any previous changes
* Start by choosing a simple image element on the page
* Pick the element using the Inspector
### Editing
* In the Element Inspector, reveal the style panel and describe its contents
* The box model representation is usually first, and provides a visual representation of the element's outline, dimensions, borders, and margins
* Next is the active style table, which lists the styles currently applied to the element, often with overridden entries indicated with a strikethrough effect
* Each active property has a name, and a single value, both described textually to the browser. Not all properties are independent (orthogonal), but will be familiar to developers with experience in desktop publishing; in these examples, we will work with absolute positioning and z-order.
* With the element selected, choose the first absolute-positioning property in the active style table, and double-click the value to edit it
### Committing
* If the element is near a corner, first move it closer to the opposite side
* Observe the results in the live view, and note that the style change was applied immediately, and that the same effect could be achieved in code (covered next)
* Finish moving the element to the corner opposite its original position.
### More Exercise
* Ask the student to repeat the exercise with other elements, making sure the elements selected are positioned absolutely, and property changes are restricted to top, left, right, bottom
* Occasionally an element will be occluded by another when moved, in these cases edit or add the z-index property to reveal the element
# Modifying Behavior
## Existing Site
### Picking
### Editing
### Committing
### More Exercise
# Introduction to Shell
