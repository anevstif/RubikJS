const nullMaterial = new THREE.MeshPhongMaterial( { color:0x333333 } ); //чёрный
const topMaterial = new THREE.MeshPhongMaterial( { color: 0xff0000 } ); //красный
const leftMaterial = new THREE.MeshPhongMaterial( { color: 0xff88ff } ); //розовый
const rightMaterial = new THREE.MeshPhongMaterial( { color: 0xffff00 } ); //жёлтый
const frontMaterial = new THREE.MeshPhongMaterial( { color: 0x00ff00 } ); //зеленый
const backMaterial = new THREE.MeshPhongMaterial( { color: 0x0000ff } ); //синий
const bottomMaterial = new THREE.MeshPhongMaterial( { color: 0x88ffff } ); //голубой




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
            //console.warn("top");
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
            //console.warn("left");
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
            //console.warn("right");
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
            //console.warn("front");
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
            //console.warn("back");
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
            //console.warn("bottom");
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
     
/*
	cubeMaterialArray.push( rightMaterial );
	cubeMaterialArray.push( leftMaterial );
	cubeMaterialArray.push( topMaterial );
	cubeMaterialArray.push( bottomMaterial );
	cubeMaterialArray.push( frontMaterial );
	cubeMaterialArray.push( backMaterial );
*/
    var cubeMaterials = new THREE.MeshFaceMaterial( cubeMaterialArray );
    return cubeMaterials
}