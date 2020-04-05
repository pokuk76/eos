/*
Extracted from tutorial <insert URL here>
*/

var hiddenClass = 'hidden';
var shownClass = 'toggled-from-hidden';

function applianceSectionHover() {
    var children = this.children;
    for(var i = 0; i < children.length; i++) {
        var child = children[i];
        if (child.className === hiddenClass) {
            child.className = shownClass;
        }
    }
}

function applianceSectionEndHover() {
    var children = this.children;
    for(var i = 0; i < children.length; i++) {
        var child = children[i];
        if (child.className === shownClass) {
            child.className = hiddenClass;
        }
    }
}

(function() {
    var applianceSections = document.getElementsByClassName('appliance');
    for(var i = 0; i < applianceSections.length; i++) {
        petSections[i].addEventListener('mouseover', applianceSectionHover);
        petSections[i].addEventListener('mouseout', applianceSectionEndHover);
    }
}());
