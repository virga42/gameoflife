function drawBoard(universe=''){
    //grid width and height
    const bw = 800;
    const bh = 600;
    //padding around grid
    const p = 10;
    //size of canvas
    let cw = bw + (p*2) + 1;
    let ch = bh + (p*2) + 1;
    //size of cell
    let ce = 20

    let canvas = document.getElementById("myCanvas");

    canvas.setAttribute("width", cw);
    canvas.setAttribute("height", ch);

    let context = canvas.getContext("2d");

    u_arr = universe.split('');
    width = 40;
    
    // clear the canvas
    context.clearRect(0, 0, canvas.width, canvas.height);

    for (let x = 0; x < u_arr.length; x++) {
      xpos = (((x % width) * ce) + p);
      ypos = (((Math.floor(x/width)) * ce) + p);
      if (u_arr[x] == 1) {
        context.fillStyle = "#f4dc42";
        context.fillRect(xpos, ypos, ce, ce);
      }
      else {
        context.fillStyle = "#e9e9e9";
        context.fillRect(xpos, ypos, ce, ce);
      }
    }

    for (let x = 0; x <= bw; x += 20) {
        context.moveTo(0.5 + x + p, p);
        context.lineTo(0.5 + x + p, bh + p);
    }

    for (let x = 0; x <= bh; x += 20) {
        context.moveTo(p, 0.5 + x + p);
        context.lineTo(bw + p, 0.5 + x + p);
    }

    context.strokeStyle = "black";
    context.stroke();
};

function postNextData(url) {
  let uni = {"universe": universe, "width": width};
  postData(url, uni);
};

function postData(url = ``, data = {}) {
    fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(data)
  })
  .then(response => response.json())
  .then(response => universe = response['universe'])
  .then(response => drawBoard(universe))
  .then(response => console.log('Success:', JSON.stringify(response)))
  .catch(error => console.error('Error:', error));
};

function getFigure(url = ``, label) {
  let figureSelector = document.getElementById("figuresDropdown");
  let selection = figureSelector.options[figureSelector.selectedIndex].value;
  url = url + '/' + selection
  fetch(url, { method: "GET" })
  .then(response => response.json())
  .then(response => universe = response['cells'])
  .then(response => drawBoard(universe))
  .then(response => console.log('Success', JSON.stringify(response)))
  .catch(error => console.error('Error', error))
};

async function createFigurePicker() {
  url = 'http://localhost:5000/api/v1/lifeforms';

  let figureList;
  try {
    figureList = await getFigureList(url);
  } catch(err) {
    console.log(err)
  }
  // let figureList = resp['list'];
  console.log(figureList['list']);

  let dropdown = document.getElementById("figuresDropdown");

  let figures = figureList['list'];
  for (f = 0; f < figures.length; f++) {
    opt = document.createElement("option");
    opt.text = figures[f]['label'];
    opt.value = figures[f]['label'];
    dropdown.options.add(opt);
  };
};

async function getFigureList(url = ``) {
  // let figureChoice = document.getElementById("figurejs");
  let response = await fetch(url, {method: "GET" });
  if (response.status == 200) {
    return response.json();
  } else {
    throw new HttpError(response);
  };
};
