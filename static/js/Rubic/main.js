/*
    ==================================================================
    functions get elements task and solver in form from server or user
 */
function getTask() {
    let elem = document.getElementById("task");
    let taskCommand;
    if (elem != null) {
        taskCommand = elem.value;
    }
    let taskCommands = (taskCommand) ? taskCommand.split(' ') : [];
    return taskCommands
}

function getSolver() {
    let elem = document.getElementById("solver");
    let solverCommand;
    if (elem != null) {
        solverCommand = elem.value;
    }
    let solverCommands = (solverCommand) ? solverCommand.split(' ') : [];
    return solverCommands
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
    console.info("result:" + result);
}

function ajaxRequest() {
    $(document).ready(function (){
        $.ajax({
            url: '/ajax',
            type: "post",
            data: "Ajax data",
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
    if (r.keyStatus != "none") {
        return;
    }
    r.updateTask(getTask());
    r.geom = new RubicGeometry(r.size);
    r.world.remup(r.size, r.geom.getGeom());
    r.keyStatus = "prepareTask";
}

function solverClick() {
    if (r.keyStatus != "endTask") {
        return;
    }
    r.updateSolver(getSolver());
    r.keyStatus = "prepareSolver";
    ajaxRequest();
}

function spdInp() {
    r.speed = document.getElementById("speed").value;
}

/*
    =======
    program
 */
var r = new Rubic();
animate();