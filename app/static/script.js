class UniverseModel {
  constructor() {
    // this.getUniverse = getUniverse;
  }
  getUniverse(universe, fn) {
    // takes a universe (cells and width) and a callback function
    console.log("input: " + JSON.stringify(universe))
    let url = 'http://localhost:5000/api/game';
    fetch(url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(universe)
    })
      .then(response => response.json())
      .then(nextUniverse => fn(nextUniverse))
      // .then(log => console.log('Success:', JSON.stringify(log)))
      // .catch(error => console.error('Error:', error));
    // fn(universe);
  }
};


class UniverseController {
  constructor(universeView, universeModel) {
    this.universeView = universeView;
    this.universeModel = universeModel;
  }
  initialize() {
    this.universeView.onClickGetNext = this.onClickGetNext.bind(this);
  }
  onClickGetNext(e) {
    console.log("e: "+ JSON.stringify(e));
    let universeRequest = {"universe": e.cells, "width": e.width}
    this.universeModel.getUniverse(universeRequest, this.showUniverse.bind(this));
  }
  showUniverse(universeModelData) {
    // I believe the intent here is to render model data to viewModel and then update the view
    let universeViewModel = {
      "cells": universeModelData.universe,
      "width": universeModelData.width
    }
    this.universeView.render(universeViewModel);
  }
};

class UniverseView {
  constructor(element) {
    this.element = element;
    // this.viewModel = {"cells": "111000111", "width": 3};
    this.onClickGetNext = null;
  }
  render(viewModel) {
    // this.element.innerHTML = '<br/><a id="nextGeneration" class="next button" href="javascript:void(0);">Next</a>'

    //grid width and height
    let boardWidth = 800;
    let boardHeight = 600;
    // padding around grid
    let padding = 10;
    // size of canvas
    let canvasWidth = boardWidth + (padding * 2) + 1;
    let canvasHeight = boardHeight + (padding * 2) + 1;

    this.element.setAttribute("width", canvasWidth);
    this.element.setAttribute("height", canvasHeight);

    let context = this.element.getContext("2d");
    // clear the canvas
    context.clearRect(0, 0, canvasWidth, canvasHeight);
    for (let x = 0; x <= boardWidth; x += 20) {
      context.moveTo(0.5 + x + padding, padding);
      context.lineTo(0.5 + x + padding, boardHeight + padding);
    }
    for (let x = 0; x <= boardHeight; x += 20) {
      context.moveTo(padding, 0.5 + x + padding);
      context.lineTo(boardWidth + padding, 0.5 + x + padding);
    }
    context.strokeStyle = "black";
    context.stroke();
    // takes a list of cell values and draws them to the board
    let cells = viewModel.cells;
    let cellSize = 20;
    let columnCount = 40;
    for (let x = 0; x < cells.length; x++) {
      let xpos = (((x % columnCount) * cellSize) + padding);
      let ypos = (((Math.floor(x / columnCount)) * cellSize) + padding);
      if (cells[x] == 1) {
        context.fillStyle = "#f4dc42";
        context.fillRect(xpos, ypos, cellSize, cellSize);
      }
      else {
        context.fillStyle = "#e9e9e9";
        context.fillRect(xpos, ypos, cellSize, cellSize);
      }
    }
    const nextGen = document.getElementById('nextGeneration');
    nextGen.addEventListener('click', function() {this.onClickGetNext(viewModel)});
  }
};

let universeModel = new UniverseModel();

let targetElement = document.getElementById('myCanvas');
let universeView = new UniverseView(targetElement);

let controller = new UniverseController(universeView, universeModel);
controller.initialize();

// let nextButton = document.getElementById('nextGeneration');

// I believe this should be the initial viewModel state
controller.onClickGetNext({"cells": "111000111", "width": 3});


function postNextData(url) {
  let uni = {"universe": universe, "width": width};
  postData(url, uni);
};


function selectFigure(url = ``, label) {
  let figureSelector = document.getElementById("figuresDropdown");
  let selection = figureSelector.options[figureSelector.selectedIndex].value;
  url = url + '/' + selection
  fetch(url, { method: "GET" })
  .then(response => response.json())
  .then(lifeform => drawBoard(lifeform.cells))
};

function createFigurePicker() {
  let url = 'http://localhost:5000/api/v1/lifeforms';

  fetch(url, { method: "GET" })
  .then(response => response.json())
  .then(figureLabels => populateDropdown(figureLabels))
}

function populateDropdown(options) {
  // view -- TODO parameterize the getElementById so this can be reused
  let dropdown = document.getElementById("figuresDropdown");

  for (f = 0; f < options.length; f++) {
    opt = document.createElement("option");
    opt.text = options[f];
    opt.value = options[f];
    dropdown.options.add(opt);
  };
}

