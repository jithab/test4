---
layout: post
title:  Least Recently Used Cache
date:   2023-11-27 12:34:56 +0000
categories: java coding
---
{% highlight java %}
class CacheNode {
    String cacheKey, cacheValue;
    CacheNode prevNode, nextNode;
}
{% endhighlight %}

{% highlight java %}
class DoubleLinkedList {

    CacheNode head = null, tail = null;

    public CacheNode add(String key, String value) {
        CacheNode node = new CacheNode();
        node.cacheKey = key;
        node.cacheValue = value;
        node.prevNode = head;

        if (head != null)
            head.nextNode = node;
        head = node;
        if (tail == null)
            tail = head;
        return node;
    }

    public CacheNode removeTailNode() {
        CacheNode tailNode = tail;
        detach(tailNode);
        return tailNode;
    }

    public void detach(CacheNode node) {
        // Remove the node from the list.
        if (node.nextNode == null)
            head = node.prevNode;
        else
            node.nextNode.prevNode = node.prevNode;

        if (node.prevNode == null)
            tail = node.nextNode;
        else
            node.prevNode.nextNode = node.nextNode;

        node.nextNode = node.prevNode = null;
    }

    public void moveToHead(CacheNode node) {
        detach(node);
        node.prevNode = head;
        head = node;
    }
}
{% endhighlight %}

{% highlight java %}
import java.util.HashMap;
import java.util.Map;

class CacheLRU {

    Map<String, CacheNode> cacheMap;
    DoubleLinkedList cacheList;
    private int cacheMaxSize;

    public CacheLRU(int size) {
        cacheMaxSize = size;
        cacheMap = new HashMap<>(cacheMaxSize);
        cacheList = new DoubleLinkedList();
    }

    public void put(String key, String value) {

        if (cacheMap.containsKey(key)) {
            // The key is already in the cache,
            // update the value and move the item to head of the list
            // to make it as most recently used item.
            CacheNode node = cacheMap.get(key);
            node.cacheValue = value;
            cacheList.moveToHead(node);
            return;
        }

        if (cacheMap.size() == cacheMaxSize) {
            // Cache is full. Remove the least recently used item,
            // which is in the tail of the list.
            CacheNode node = cacheList.removeTailNode();
            cacheMap.remove(node.cacheKey);
        }

        // Add item to cache
        CacheNode node = cacheList.add(key, value);
        cacheMap.put(key, node);
    }

    public String get(String key) {
        CacheNode node = cacheMap.get(key);
        if (node == null) return null;

        // Move the accessed item to head of the list
        // to make it as the most recently used item.
        cacheList.moveToHead(node);

        return node.cacheValue;
    }
}
{% endhighlight %}

{% highlight java %}
class Main {
    public static void main(String[] args) {

        CacheLRU cache = new CacheLRU(3);

        cache.put("key1", "value1");    // k1
        cache.put("key2", "value2");    // k1 k2
        cache.put("key3", "value3");    // k1 k2 k3
        cache.put("key1", "value1New"); // k2 k3 k1
        cache.get("key2");              // k3 k1 k2
        cache.put("key4", "value4");    // k1 k2 k4

        print("value1New".equals(cache.get("key1")));
        print("value2".equals(cache.get("key2")));
        print(null == cache.get("key3"));
        print("value4".equals(cache.get("key4")));
    }

    private static void print(boolean success) {
        System.out.println(success ? "Ok" : "Failed!");
    }
}
{% endhighlight %}