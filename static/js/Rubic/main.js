function getTaskSolver() {
    let elem = document.getElementById("task");
    let taskCommand;
    if (elem != null) {
        taskCommand = elem.innerHTML;
    }
    let solverCommand;
    elem = document.getElementById("solver");
    if (elem != null) {
        solverCommand = elem.innerHTML;
    }
    let taskCommands = (taskCommand) ? taskCommand.split(' ') : [];
    let solverCommands = (solverCommand) ? solverCommand.split(' ') : [];
    return {task: taskCommands, solver: solverCommands}
}

function animate()
{
    r.update();
    requestAnimationFrame( animate );
}

function startClick() {
    r.updateTaskSolver();
    r.geom = new RubicGeometry(r.size);
    r.world.remup(r.size, r.geom.getGeom());
    r.keyStatus = "startTask";
}

function spdInp() {
    r.speed = document.getElementById("speed").value;
}

function solverClick() {
    r.keyStatus = "startSolver";
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
function afterSend(result) {
    console.info("result:" + result);
}

var r = new Rubic();
animate();