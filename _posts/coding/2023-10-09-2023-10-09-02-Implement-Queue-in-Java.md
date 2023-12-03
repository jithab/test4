---
layout: post
title:  Implement Queue in Java
date:   2023-10-09 02:38:00 +0000
categories: java coding
type: coding
---

{% highlight java %}
package in.perwad.queue;

public class Main {
    public static void main(String[] args) {

        Stack<Integer> stack = new Stack<>();

        for(int item : new int [] {321, 123, 231})
            stack.enqueue(item);

        while (!stack.empty())
            System.out.println(stack.dequeue());
            // output: 321, 123, 231
    }
}
{% endhighlight %}

{% highlight java %}
class Stack<ItemDataType>  {
    Item<ItemDataType> front = null;
    Item<ItemDataType> rear = null;

    public void enqueue(ItemDataType data) {
        Item<ItemDataType> item = new Item<>(data, rear);
        if(rear != null)
            rear.setPrevItem(item);
        rear = item;
        if(front == null)
            front = rear;
    }

    public ItemDataType dequeue() {
        ItemDataType data = front.getData();
        front = front.getPrevItem();
        return data;
    }

    public boolean empty() {
        return front == null;
    }

}
{% endhighlight %}

{% highlight java %}
class Item<DataType>  {

    private final DataType data;
    private Item prevItem;
    private final Item nextItem;

    public Item(DataType data,  Item nextItem) {
        this.data = data;
        this.nextItem = nextItem;
    }

    public DataType getData() {
        return data;
    }

    public void setPrevItem(Item prevItem) {
        this.prevItem = prevItem;
    }

    public Item getPrevItem() {
        return prevItem;
    }

}
{% endhighlight %}