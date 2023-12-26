package DSA.Java.Stacks;

class stackProblems {
    public static void main(String[] args) {
        Stack<Integer> s = new Stack<Integer>(5);
        System.out.println(s);
        s.push(1);
        System.out.println(s);
        s.push(1);
        System.out.println(s);
        s.push(1);
        System.out.println(s);
        s.push(1);
        System.out.println(s);
        s.push(314);
        System.out.println(s);
        s.push(314);
        s.push(314);
        s.push(314);
        s.push(314);
        s.push(314);
        s.push(314);
        s.push(314);
        s.push(314);
        s.push(314);
        System.out.println(s + ", " + s.maxSize);
    }
}