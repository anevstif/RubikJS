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
        this.scene.add(addLight(size));
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
	    /*
        if ( this.keyboard.pressed("1") )
		    console.debug('press 1');
	    if ( this.keyboard.pressed("2") )
		    console.debug('press 2');
        */
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

function addLight(size) {
    var light = new THREE.Object3D();
    var dist = 0.8 * size;
	var lf = new THREE.PointLight(0xffffff);
    var lb = new THREE.PointLight(0xffffff);
    var lr = new THREE.PointLight(0xffffff);
    var ll = new THREE.PointLight(0xffffff);
    var lu = new THREE.PointLight(0xffffff);
    var ld = new THREE.PointLight(0xffffff);
    light.add(lf);
    light.add(lb);
    light.add(lr);
    light.add(ll);
    light.add(lu);
    light.add(ld);
    lf.position.set(0, 0, dist);
    lb.position.set(0,0,-dist);
    ll.position.set(-dist, 0, 0);
    lr.position.set(dist,0, 0);
    lu.position.set(0, dist, 0);
    ld.position.set(0,-dist, 0);
    return light
}
