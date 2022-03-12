
const normMap = THREE.ImageUtils.loadTexture( 'static/images/normal.png' );
const nullMaterial = new THREE.MeshPhongMaterial( { map: THREE.ImageUtils.loadTexture( 'static/images/inner.png' ) });
const topMaterial = new THREE.MeshPhongMaterial( { map: THREE.ImageUtils.loadTexture( 'static/images/up.png' ), normalMap: normMap });
const leftMaterial = new THREE.MeshPhongMaterial( { map: THREE.ImageUtils.loadTexture( 'static/images/left.png' ), normalMap: normMap  });
const rightMaterial = new THREE.MeshPhongMaterial( { map: THREE.ImageUtils.loadTexture( 'static/images/right.png' ), normalMap: normMap  });
const frontMaterial = new THREE.MeshPhongMaterial( { map: THREE.ImageUtils.loadTexture( 'static/images/front.png' ), normalMap: normMap  });
const backMaterial = new THREE.MeshPhongMaterial( { map: THREE.ImageUtils.loadTexture( 'static/images/back.png' ), normalMap: normMap  });
const bottomMaterial = new THREE.MeshPhongMaterial( { map: THREE.ImageUtils.loadTexture( 'static/images/down.png' ), normalMap: normMap  });


function createCubeMaterial(boxType, side) {
    // Create an array of materials to be used in a cube, one for each side
	var cubeMaterialArray = [];
	// order to add materials: x+,x-,y+,y-,z+,z-
    cubeMaterialArray.push( nullMaterial );
	cubeMaterialArray.push( nullMaterial );
	cubeMaterialArray.push( nullMaterial );
	cubeMaterialArray.push( nullMaterial );
	cubeMaterialArray.push( nullMaterial );
	cubeMaterialArray.push( nullMaterial );

    switch (side) {
        case Side.Top:
            cubeMaterialArray[2] = topMaterial;
            switch (boxType) {
                case BoxType.EdgeTop:
                    cubeMaterialArray[5] = backMaterial;
                    break;
                case BoxType.EdgeLeft:
                    cubeMaterialArray[1] = leftMaterial;
                    break;
                case BoxType.EdgeRight:
                    cubeMaterialArray[0] = rightMaterial;
                    break;
                case BoxType.EdgeBottom:
                    cubeMaterialArray[4] = frontMaterial;
                    break;
                case BoxType.CornerTopLeft:
                    cubeMaterialArray[5] = backMaterial;
                    cubeMaterialArray[1] = leftMaterial;
                    break;
                case BoxType.CornerTopRight:
                    cubeMaterialArray[5] = backMaterial;
                    cubeMaterialArray[0] = rightMaterial;
                    break;
                case BoxType.CornerBottomLeft:
                    cubeMaterialArray[4] = frontMaterial;
                    cubeMaterialArray[1] = leftMaterial;
                    break;
                case BoxType.CornerBottomRight:
                    cubeMaterialArray[4] = frontMaterial;
                    cubeMaterialArray[0] = rightMaterial;
            }
            break;
        case Side.Left:
            cubeMaterialArray[2] = leftMaterial;
            switch (boxType) {
                case BoxType.EdgeTop:
                    cubeMaterialArray[5] = backMaterial;
                    break;
                case BoxType.EdgeLeft:
                    cubeMaterialArray[1] = bottomMaterial;
                    break;
                case BoxType.EdgeRight:
                    cubeMaterialArray[0] = topMaterial;
                    break;
                case BoxType.EdgeBottom:
                    cubeMaterialArray[4] = frontMaterial;
                    break;
                case BoxType.CornerTopLeft:
                    cubeMaterialArray[5] = backMaterial;
                    cubeMaterialArray[1] = bottomMaterial;
                    break;
                case BoxType.CornerTopRight:
                    cubeMaterialArray[5] = backMaterial;
                    cubeMaterialArray[0] = topMaterial;
                    break;
                case BoxType.CornerBottomLeft:
                    cubeMaterialArray[4] = frontMaterial;
                    cubeMaterialArray[1] = bottomMaterial;
                    break;
                case BoxType.CornerBottomRight:
                    cubeMaterialArray[4] = frontMaterial;
                    cubeMaterialArray[0] = topMaterial;
            }
            break;
        case Side.Right:
            cubeMaterialArray[2] = rightMaterial;
            switch (boxType) {
                case BoxType.EdgeTop:
                    cubeMaterialArray[5] = backMaterial;
                    break;
                case BoxType.EdgeLeft:
                    cubeMaterialArray[1] = topMaterial;
                    break;
                case BoxType.EdgeRight:
                    cubeMaterialArray[0] = bottomMaterial;
                    break;
                case BoxType.EdgeBottom:
                    cubeMaterialArray[4] = frontMaterial;
                    break;
                case BoxType.CornerTopLeft:
                    cubeMaterialArray[5] = backMaterial;
                    cubeMaterialArray[1] = topMaterial;
                    break;
                case BoxType.CornerTopRight:
                    cubeMaterialArray[5] = backMaterial;
                    cubeMaterialArray[0] = bottomMaterial;
                    break;
                case BoxType.CornerBottomLeft:
                    cubeMaterialArray[4] = frontMaterial;
                    cubeMaterialArray[1] = topMaterial;
                    break;
                case BoxType.CornerBottomRight:
                    cubeMaterialArray[4] = frontMaterial;
                    cubeMaterialArray[0] = bottomMaterial;
            }
            break;
        case Side.Front:
            cubeMaterialArray[2] = frontMaterial;
            switch (boxType) {
                case BoxType.EdgeTop:
                    cubeMaterialArray[5] = rightMaterial;
                    break;
                case BoxType.EdgeLeft:
                    cubeMaterialArray[1] = leftMaterial;
                    break;
                case BoxType.EdgeRight:
                    cubeMaterialArray[0] = rightMaterial;
                    break;
                case BoxType.EdgeBottom:
                    cubeMaterialArray[4] = leftMaterial;
                    break;
                case BoxType.CornerTopLeft:
                    cubeMaterialArray[5] = rightMaterial;
                    cubeMaterialArray[1] = topMaterial;
                    break;
                case BoxType.CornerTopRight:
                    cubeMaterialArray[5] = rightMaterial;
                    cubeMaterialArray[0] = bottomMaterial;
                    break;
                case BoxType.CornerBottomLeft:
                    cubeMaterialArray[4] = leftMaterial;
                    cubeMaterialArray[1] = topMaterial;
                    break;
                case BoxType.CornerBottomRight:
                    cubeMaterialArray[4] = leftMaterial;
                    cubeMaterialArray[0] = bottomMaterial;
            }
            break;
        case Side.Back:
            cubeMaterialArray[2] = backMaterial;
            switch (boxType) {
                case BoxType.EdgeTop:
                    cubeMaterialArray[5] = leftMaterial;
                    break;
                case BoxType.EdgeLeft:
                    cubeMaterialArray[1] = leftMaterial;
                    break;
                case BoxType.EdgeRight:
                    cubeMaterialArray[0] = rightMaterial;
                    break;
                case BoxType.EdgeBottom:
                    cubeMaterialArray[4] = rightMaterial;
                    break;
                case BoxType.CornerTopLeft:
                    cubeMaterialArray[5] = leftMaterial;
                    cubeMaterialArray[1] = topMaterial;
                    break;
                case BoxType.CornerTopRight:
                    cubeMaterialArray[5] = leftMaterial;
                    cubeMaterialArray[0] = bottomMaterial;
                    break;
                case BoxType.CornerBottomLeft:
                    cubeMaterialArray[4] = rightMaterial;
                    cubeMaterialArray[1] = topMaterial;
                    break;
                case BoxType.CornerBottomRight:
                    cubeMaterialArray[4] = rightMaterial;
                    cubeMaterialArray[0] = bottomMaterial;
            }
            break;
        case Side.Bottom:
            cubeMaterialArray[2] = bottomMaterial;
            switch (boxType) {
                case BoxType.EdgeTop:
                    cubeMaterialArray[5] = backMaterial;
                    break;
                case BoxType.EdgeLeft:
                    cubeMaterialArray[1] = rightMaterial;
                    break;
                case BoxType.EdgeRight:
                    cubeMaterialArray[0] = leftMaterial;
                    break;
                case BoxType.EdgeBottom:
                    cubeMaterialArray[4] = frontMaterial;
                    break;
                case BoxType.CornerTopLeft:
                    cubeMaterialArray[5] = backMaterial;
                    cubeMaterialArray[1] = rightMaterial;
                    break;
                case BoxType.CornerTopRight:
                    cubeMaterialArray[5] = backMaterial;
                    cubeMaterialArray[0] = leftMaterial;
                    break;
                case BoxType.CornerBottomLeft:
                    cubeMaterialArray[4] = frontMaterial;
                    cubeMaterialArray[1] = rightMaterial;
                    break;
                case BoxType.CornerBottomRight:
                    cubeMaterialArray[4] = frontMaterial;
                    cubeMaterialArray[0] = leftMaterial;
            }
    }

    var cubeMaterials = new THREE.MeshFaceMaterial( cubeMaterialArray );
    return cubeMaterials
}