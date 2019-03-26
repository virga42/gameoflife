function createTextRenderer() {
  return {
    characters: "",
    charactersArray: [[]],
    width: 0,
    height: 0,

    draw: function(livingCells) {
      let textUniverse = "";
      if (livingCells.length > 0) {
        textUniverse = "1";
      }
      //   for (let [cellX, cellY] of livingCells) {
      //     let textCell = cellX + ", " + cellY;
      //     textUniverse += textCell;
      //   }
      return textUniverse;
    },

    placeCharacter: function(character, x , y) {
      // store a character so it can be drawn
      if (arguments.length === 1) {
        x = 0;
        y = 0;
      }
      this.width = Math.max(this.width, (x + 1));
      this.characters += character;
    },

    placeCharacterNew: function(character, x = 0, y = 0) {
      let originalHeight = this.height;
      let originalWidth = this.width;

      // pad rows, if necessary
      if (y > (this.height - 1)) {
        for (let h = originalHeight; h <= y; h++) {
          this.charactersArray.push([])
        }
      }

      this.height = Math.max(this.height, (y + 1));


      // pad columns, if necessary
      for (let j = 0; j < this.height; j++) {
        if (x > (this.width - 1)) {
          for (let i = this.width; i <= x; i++) {
            this.charactersArray[j][i] = " ";
          }
        }
      }

      this.charactersArray[y][x] = character;
      this.characters = "";

      this.width = Math.max(this.width, (x + 1));


      for (let k = 0; k < this.charactersArray.length; k++) {
        this.characters += this.charactersArray[k].join("");
      }
    },

    drawNew: function() {
      let screen = "";
      for (let i = 0; i < this.characters.length; i++) {
        if (i % this.width === 0 && i > 0) {
          screen += "\n";
        } 
        screen += this.characters[i];
      }
      return screen;
    }
  };
}

module.exports = { createTextRenderer: createTextRenderer };
