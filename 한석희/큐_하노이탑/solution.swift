
class Tower {
    
    public var disks : [Int]
    private var index : Int
    
    public init(index : Int){
        
        self.disks = []
        self.index = index
        
    }
    
    public func towerIndex() -> Int {
        return self.index
    }
    
    public func add(newDisk : Int){
        
        if !disks.isEmpty && disks.last! <= newDisk {
            fatalError("Error placing disk to tower : \(self.index)")
        }
        else{
            disks.append(newDisk)
        }
    
    }
    
    //
    public func moveTopTo(t : Tower){
        if let top = disks.popLast() {
            t.add(newDisk: top)
        }
    }
    
    //
    public func moveDisks(n : Int, destination : Tower, buffer : Tower){
        if n > 0 {
            moveDisks(n: n - 1, destination: buffer, buffer: destination)
            moveTopTo(t: destination)
            buffer.moveDisks(n: n - 1 , destination: destination, buffer: self)
        }
    }
    
}

// put how many disks in total
let n = 3
var towers : [Tower] = []
for i in (0...2){
    towers.append( Tower(index: i) )
}
for k in (0...2){
    var i = k
    i = 3 - i
    towers[0].add(newDisk: i)
}
towers[0].moveDisks( n: n, destination: towers[2], buffer: towers[1] )
towers[2].disks

