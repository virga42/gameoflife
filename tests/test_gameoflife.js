const GameOfLife = require("../app/static/gameoflife");
const textDisplayExports = require("../app/static/textDisplay");

// const testUniverseGeneration = new GameOfLife(
//   mockUniverseGenerator({ "universe:": "010000010", width: 3 }),
//   mockUniverseDisplay("111000111")
// );

// function mockUniverseGenerator(expectedLifeform) {
//   return {
//     getUniverse: function(lifeform) {
//       return expectedLifeform;
//     }
//   };
// }

function mockUniverseDisplay(expectedTextUniverse) {
  return {
    displayUniverse: function() {
      return expectedTextUniverse;
    }
  };
}

// describe("creating universe model", () => {
//   test("getting next universe", () => {
//     expect(
//       testUniverseGeneration.getUniverse({ universe: "111000111", width: 3 })
//     ).toEqual({ "universe:": "010000010", width: 3 });
//   });
// });

function initializeGameOfLife() {
  return new GameOfLife(textDisplayExports.createTextRenderer());
}

describe("displaying universe in text format", () => {
  let gol = initializeGameOfLife();

  test("can render an empty universe ", () => {
    gol.initialize();
    expect(gol.displayUniverse()).toEqual("");
  });
  test("can render a universe with a single cell ", () => {
    let singleCell = [0, 0];
    gol.initialize([singleCell]);
    expect(gol.displayUniverse()).toEqual("1");
  });
  // test("can render a universe with a single cell ", () => {
  //   let singleCell = [1, 0];
  //   gol.initialize([singleCell]);
  //   expect(gol.displayUniverse()).toEqual("1");
  // });
  // test("can render a universe with multiple cells ", () => {
  //   let multipleCells = [[0, 0], [1, 1]];
  //   gol.initialize(multipleCells);
  //   expect(gol.displayUniverse()).toEqual("0, 0/n1, 1");
  // });
});

describe("create a text renderer", () => {
  test("can create emptiness", () => {
    let textRenderer = new  textDisplayExports.createTextRenderer();
    expect(textRenderer.drawNew()).toEqual("");
  })
  test("can output a character at a default position", () => {
    let textRenderer = new  textDisplayExports.createTextRenderer();
    textRenderer.placeCharacterNew("0")
    expect(textRenderer.drawNew()).toEqual("0");
  })
  test("can output a character at given position", () => {
    let textRenderer = new  textDisplayExports.createTextRenderer();
    let x = 0
    let y = 0
    textRenderer.placeCharacterNew("0", x, y)
    expect(textRenderer.drawNew()).toEqual("0");

    x = 1
    y = 0
    textRenderer.placeCharacterNew("1", x, y)
    expect(textRenderer.drawNew()).toEqual("01");

    x = 0
    y = 1
    textRenderer.placeCharacterNew("2", x, y)
    expect(textRenderer.drawNew()).toEqual("01\n2");

    x = 1
    y = 1
    textRenderer.placeCharacterNew("3", x, y)
    expect(textRenderer.drawNew()).toEqual("01\n23");

    x = 3
    y = 1
    textRenderer.placeCharacterNew("4", x, y)
    expect(textRenderer.drawNew()).toEqual("01  \n23 4");
  })
  
})

describe("initializing Game of Life", () => {
  test("can initialize empty population", () => {
    let gol = new GameOfLife();
    gol.initialize();
    expect(gol.numberLiveCells()).toEqual(0);
    expect(gol.coordinatesLiveCells()).toEqual([]);
  });
  test("can initialize population of given size", () => {
    let gol = new GameOfLife();
    let size = 2;
    let liveCells = [[0, 0], [1, 1]];
    gol.initialize(liveCells);
    expect(gol.numberLiveCells()).toEqual(size);
    expect(gol.coordinatesLiveCells()).toEqual(liveCells);
  });
});

describe("adding cells to population", () => {
  test("can breed a single cell", () => {
    let gol = new GameOfLife();
    gol.initialize();
    let newbornCell = [[1, 1]];
    gol.breedCells(newbornCell);
    expect(gol.numberLiveCells()).toEqual(1);
    expect(gol.coordinatesLiveCells()).toEqual(newbornCell);
  });
  test("can breed multiple cells", () => {
    let gol = new GameOfLife();
    gol.initialize();
    let multipleNewbornCells = [[1, 1], [2, 1], [3, 1]];
    gol.breedCells(multipleNewbornCells);
    expect(gol.numberLiveCells()).toEqual(3);
    expect(gol.coordinatesLiveCells()).toEqual(multipleNewbornCells);
  });
  test("can add a cell that already exists", () => {
    let gol = new GameOfLife();
    let liveCells = [[0, 0]];
    gol.initialize(liveCells);
    gol.breedCells(liveCells); // add a cell at the same location
    expect(gol.numberLiveCells()).toEqual(1);
    expect(gol.coordinatesLiveCells()).toEqual(liveCells);
  });
});
