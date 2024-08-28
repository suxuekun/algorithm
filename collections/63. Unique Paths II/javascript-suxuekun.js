/**
 * @param {number[][]} obstacleGrid
 * @return {number}
 */
var uniquePathsWithObstacles = function(obstacleGrid) {
    var m = obstacleGrid.length;
    var n = obstacleGrid[0].length;
    console.log(m,n);
    var matrix = [];
    var i,j,k;
    for (i=0;i<m;i++){
        matrix[i] = [];
        for (j=0;j<n;j++){
            if (obstacleGrid[i][j] == 1){
                matrix[i][j] = 0;
            }else{
                if (i>0){
                    if (j>0){
                        matrix[i][j] = matrix[i-1][j] + matrix[i][j-1];
                    }else{
                        matrix[i][j] = matrix[i-1][j];
                    }
                }else{
                    if (j>0){
                        matrix[i][j] = matrix[i][j-1];
                    }else{
                        matrix[i][j] = 1;
                    }
                } 
            }
        }
    }
    return matrix[m-1][n-1];
    
};