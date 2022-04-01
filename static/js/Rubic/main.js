/*
    ==================================================================
    functions get elements task and solver in form from server or user
 */
function getTask(task) {
    let elem = document.getElementById("task");
    let taskCommand;
    if (elem != null) {
        if (task) {
            taskCommand = task;
            elem.value = task;
        } else {
            taskCommand = elem.value;
        }
    }
    let taskCommands = (taskCommand) ? taskCommand.split(' ') : [];
    return taskCommands;
}

function getSolver(solver) {
    let elem = document.getElementById("solver");
    let solverCommand;
    if (elem != null) {

    }
    if (elem != null) {
        if (solver) {
            solverCommand = solver;
            elem.value = solver;
        } else {
            solverCommand = elem.value;
        }
    }
    let solverCommands = (solverCommand) ? solverCommand.split(' ') : [];
    solverCount = document.getElementById("HTM");
    solverCount.innerHTML = "HTM: " + solverCommands.length + " steps";
    return solverCommands;
}

/*
=================
    infinite loop
 */
function animate()
{
    r.update();
    requestAnimationFrame( animate );
}

/*
    ==============
    ajax functions
 */
function afterSend(result) {
    let jsonObj = JSON.parse(result, (key, value) => {
        return value;
    });
    console.info("task:" + jsonObj.task + ";\nsolution:" + jsonObj.solution);
    r.updateTask(getTask(jsonObj.task));
    r.updateSolver(getSolver(jsonObj.solution));
    r.geom = new RubicGeometry(r.size);
    r.world.remup(r.size, r.geom.getGeom());
    r.keyStatus = r_keyStatus_prepareTask;
}

function ajaxRequest(dataTask) {
    console.info("start data:" + dataTask)
    $(document).ready(function (){
        $.ajax({
            url: '/ajax'+String(r.size),
            type: "post",
            data: dataTask,
            dataType: 'html',
            beforeSend: function() {
                console.info("loading...");
            },
            success: afterSend
        });
    });
}

/*
    ============================
    listeners from form elements
 */
function startClick() {
    if (r.keyStatus != r_keyStatus_none) {
        //return;
    }
    let tasks = getTask().join(" ");
    ajaxRequest(tasks);
}

function solverClick() {
    if (r.keyStatus != r_keyStatus_endTask) {
        //return;
    }
    r.updateSolver(getSolver());
    r.keyStatus = r_keyStatus_prepareSolver;
}

function getRandomInt(max) {
    return Math.floor(Math.random() * max);
}

function generateClick() {
    face = ["U", "D", "F", "B", "L", "R"];
    dir = ["", "'", "2"];
    s = "";
    lenScramble = getRandomInt(100) + 1;
    for (i = 0; i < lenScramble; i++) {
        s = s + " " + face[getRandomInt(6)] + dir[getRandomInt(3)];
    }
    let elem = document.getElementById("task");
    elem.value = s.trim();
}

function animateClick(value) {
    document.getElementById("anim").innerHTML = value.checked;
    anim = value.checked;
    if (anim) {
        r.speed = document.getElementById("speed").value;
        r.animate = true;
    } else {
        r.speed = 1000;
        r.animate = false;
    }
}

function spdInp() {
    anim = document.getElementById("anim").value;
    if (anim) {
        r.speed = document.getElementById("speed").value;
    }
}

/*
    =======
    program
 */
size = document.getElementById("size").innerHTML
var r = new Rubic(size);
animate();