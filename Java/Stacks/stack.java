package DSA.Java.Stacks;
import java.util.EmptyStackException;
public class Stack<T> {
    private int size;
    public int maxSize;
    private int topIdx;
    private Object[] data;
    private static double LF = 0.5;

    public Stack(int size) {
        this.maxSize = size;
        this.size = 0;
        this.topIdx = 0;
        this.data = new Object[size];
    }

    public void push(T item) {
        this.resize();
        if ((this.size + 1) <= this.maxSize) {
            this.data[this.topIdx++] = item; 
            this.size++;
        } else throw new IllegalStateException("Stack Overflow");
    }

    public T top() {
        if (!this.isEmpty()) {
            return (T) this.data[this.topIdx];
        } else throw new EmptyStackException();
    }

    public void pop() {
        if (!this.isEmpty()) {
            this.size--;
            this.topIdx--;
        } else throw new EmptyStackException();
    }

    public boolean isEmpty() {
        return size == 0;
    }

    public String toString() {
        String res = "[";
        if (this.size == 0) return res += "]";

        for (int i = 0; i < size; i++) {
            if (i == size - 1) {
                res += this.data[i] + "]";
            }
            else res += this.data[i] + ", ";
        }
        return res;
    }

    private void resize() {
        /** If the size is past the LF, then resize */
        if (this.maxSize * LF <= this.size) {
            /** Copy into new array */
            Object[] newStack = new Object[this.maxSize * 2];
            for (int i = 0; i < this.maxSize; i++) {
                newStack[i] = this.data[i];
            }
            this.maxSize *= 2;
            this.data = newStack;
        } else return;
    }
}