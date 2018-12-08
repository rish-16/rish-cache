var Stylus = function(element) {
    this.name = element
    this.element = $(element)
}

Stylus.prototype.addStyle = function(config) {
    // Adding styles to element
    for (var i = 0; i < Object.keys(config).length; i++) {
        this.element.css(Object.keys(config)[i], Object.values(config)[i])
    }
}

Stylus.prototype.style = function(value) {
    // Getting the specific style of an element
    return this.element.css(value)
}

Stylus.prototype.inherit = function(copyElement, property='all') {
    let elementStyles
    if (typeof copyElement == 'object') {
        // If the parameter is a Stylus object
        elementStyles = window.getComputedStyle(document.querySelector(copyElement.name))
    } else if (typeof copyElement == 'string') {
        // If the parameter is a tag/id/class name
        elementStyles = window.getComputedStyle(document.querySelector(copyElement))
    }

    if (property == 'all') {
        // Inherit all CSS properties from copyElement
        for (var i = 0; i < elementStyles.length; i++) {
            var prop = elementStyles[i]
            this.element.css(prop, elementStyles[prop])
        }        
    } else {
        // Inherit specific CSS property from copyElement
        this.element.css(property, elementStyles[property])
    }
}