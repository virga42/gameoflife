const GameOfLife = require("../app/static/gameoflife");

const testUniverseGeneration = new GameOfLife(
  mockUniverseGenerator({ "universe:": "010000010", width: 3 }),
  mockUniverseDisplay("111000111")
);

function mockUniverseGenerator(expectedLifeform) {
  return {
    getUniverse: function(lifeform) {
      return expectedLifeform;
    }
  };
}

function mockUniverseDisplay(expectedTextUniverse) {
  return {
    displayUniverse: function(universe) {
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

// describe("displaying universe as text", () => {
//   test("rendering universe as ASCII", () => {
//     expect(testUniverseGeneration.displayUniverse()).toEqual(
//       "111000111"
//     );
//   });
// });

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
    gol.breedCells(liveCells);
    expect(gol.numberLiveCells()).toEqual(1);
    expect(gol.coordinatesLiveCells()).toEqual(liveCells);
  })
});
