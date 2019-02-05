* freeze selection that is highlighted
* add button to play and pause (anything 10 fps or better)
** javascript animation frame window.request animation frame

* static repository (zoo) of lifeforms

* push a lifeform into zoo with label (i.e. glider) and namespace (e.g. tom.glider, alex.glider). Namespace must be enforced
** takes fully qualified namespaced label
** takes a board
** collision with namespace & label
** ability to overwrite lifeforms
** ability to remove a lifeform
** ability to get a list of lifeforms available
** persist zoo as text file (expect hundreds of lifeforms)
** max area 10,000 x 10,000 per lifeform

* API get a lifeform
** with namespace returns exact lifeform or nothing
** no namespace returns first found or nothing

