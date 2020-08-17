class Solution {
    func maxSumSubmatrix(_ matrix: [[Int]], _ k: Int) -> Int {
        
        
        let rowNum = 0...(matrix.count - 1) // row indices
        let colNum = 0...(matrix[0].count - 1) // col indices
        
        // two rows combinations
        var rowCombs : [ (Int, Int) ] = []
        for i in rowNum {
            for j in rowNum where j >= i {
                rowCombs.append( (i, j) )
            }
        }
        
        // two columns combinations
        var colCombs : [ (Int, Int) ] = []
        for i in colNum {
            for j in colNum where j >= i {
                colCombs.append( (i, j) )
            }
        }
        
        // with different set of rowCombs & colCombs
            // 1). find four points sums
            // 2). and append
        var possibleSums = [ Int ]()
        
        // for given matrix => get all possible rectangle sums
        for aRowComb in rowCombs {
            for aColComb in colCombs {
            
                if aRowComb.0 != aRowComb.1 &&
                    aColComb.0 != aColComb.1 {
                        var aSum = 0
                        for i in (aRowComb.0 ... aRowComb.1){
                            for j in (aColComb.0...aColComb.1){
                                aSum += matrix[i][j]
                            }
                        }
                        possibleSums.append(aSum)
                    }
                
                else if aRowComb.0 == aRowComb.1 &&
                aColComb.0 != aColComb.1 {
                    var aSum = 0
                    let rowIndex = aRowComb.0
                    for i in (aColComb.0...aColComb.1){
                        aSum += matrix[rowIndex][i]
                    }
                    possibleSums.append(aSum)
                }
                
                else if aRowComb.0 != aRowComb.1 &&
                aColComb.0 == aColComb.1 {
                    var aSum = 0
                    let colIndex = aColComb.0
                    for i in (aRowComb.0...aRowComb.1){
                        aSum += matrix[i][colIndex]
                    }
                    possibleSums.append(aSum)
                }
                else if aRowComb.0 == aRowComb.1 &&
                    aColComb.0 == aColComb.1 {
                    possibleSums.append( matrix[aRowComb.0][aColComb.0] )
                }
        
            }
        
        }
        
        
        return possibleSums.filter{ $0 <= k }.max()!
    }
    
}



