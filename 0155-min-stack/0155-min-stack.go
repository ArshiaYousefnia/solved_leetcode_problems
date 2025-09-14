type MinStack struct {
    items [][2]int
}


func Constructor() MinStack {
    items := make([][2]int, 0)

    return MinStack{
        items: items,
    }
}


func (this *MinStack) Push(val int)  {
    if (len(this.items) == 0) {
        this.items = append(this.items, [2]int{val, val})
    } else {
        this.items = append(this.items, [2]int{val, min(val, this.items[len(this.items)-1][1])})
    }
}


func (this *MinStack) Pop()  {
    if (len(this.items) != 0) {
        this.items = this.items[:len(this.items)-1]
    }
}


func (this *MinStack) Top() int {
    if (len(this.items) == 0) {
        return 0
    }
    return this.items[len(this.items)-1][0]
}


func (this *MinStack) GetMin() int {
    if (len(this.items) == 0) {
        return 0
    }
    return this.items[len(this.items)-1][1]
}


/**
 * Your MinStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(val);
 * obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.GetMin();
 */