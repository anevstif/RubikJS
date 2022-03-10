class World {
    constructor(size, geometry) {        
        this.size = size;
        this.keyboard = new THREEx.KeyboardState();
        this.clock = new THREE.Clock();
        this.scene = new THREE.Scene();
        this.camera = createCamera(size)
        this.scene.add(this.camera);
        this.camera.lookAt(this.scene.position);
        this.renderer = createRenderer()
        THREEx.WindowResize(this.renderer, this.camera);
        THREEx.FullScreen.bindKey({ charCode : 'm'.charCodeAt(0) });
	    this.controls = new THREE.OrbitControls( this.camera, this.renderer.domElement );  
        this.scene.add(addLight());
        this.geom = geometry;
        this.rubic = new THREE.Object3D();
        this.rubic.add(this.geom);
        this.scene.add(this.rubic);

        var axis = new THREE.AxisHelper(10);
        this.scene.add(axis);
    }

    remup(size, geometry) {
        var deltaSize = size / this.size;
        this.size = size;
        this.camera.position.set(this.camera.position.x * deltaSize, this.camera.position.y * deltaSize, this.camera.position.z * deltaSize);
        this.rubic.remove(this.geom);
        this.geom = geometry;
        this.rubic.add(this.geom);
    }

    update()
    {
	    // delta = change in time since last call (in seconds)
	    //var delta = this.clock.getDelta(); 
	    /*
        if ( this.keyboard.pressed("1") )
		    console.debug('press 1');
	    if ( this.keyboard.pressed("2") )
		    console.debug('press 2');
        //*/
        this.controls.update();
        var delta = this.clock.getDelta();
        return delta;
        
        //this.geom.rotation.x += delta * THREE.Math.degToRad(30)
        //this.geom.rotation.y += delta * THREE.Math.degToRad(45)
    }

    render() 
    {	
	    this.renderer.render( this.scene, this.camera );
    }
}

function createCamera(size) {
    var camera;
	var VIEW_ANGLE = 45, ASPECT = window.innerWidth / window.innerHeight, NEAR = 0.01, FAR = 200;
	camera = new THREE.PerspectiveCamera( VIEW_ANGLE, ASPECT, NEAR, FAR);
    camera.position.set(1.5 * size, 1.5*size, size * 3);
    return camera;
}

function createRenderer() {    
    var renderer;
    if ( Detector.webgl )
        renderer = new THREE.WebGLRenderer( {antialias:true} );
    else
        renderer = new THREE.CanvasRenderer(); 
    renderer.setSize(window.innerWidth, window.innerHeight);
    //container = document.getElementById( 'scene-container' );
    container = document.createElement( 'div' );
    container.setAttribute("id","scene-container");
	document.body.appendChild( container );
    container.appendChild( renderer.domElement );
    return renderer
}

function addLight() {
    var light = new THREE.Object3D();
    var l1 = new THREE.DirectionalLight(0xffffff, 1);
	var l2 = new THREE.PointLight(0xffffff);
    var l3 = new THREE.PointLight(0xffffff);
    light.add(l1);
    light.add(l2);
    light.add(l3);
    l2.position.set(25,25,20);
    l3.position.set(-25,-25,-20);
    return light
}
