import java.lang.Math;
class Main {
    public static void main(String[] args) {
        MyPoint p = new MyPoint();
        // MyPoint p2 = new MyPoint(1.5, -7);
        // System.out.println(p.distance(p2));
        // System.out.println(p.toString());
        // System.out.println(p2.toString());
        MyPoint[] ps = new MyPoint[6];
        ps[0] = new MyPoint();
        ps[1] = new MyPoint(1, 1);
        ps[2] = new MyPoint(2, 3);
        ps[3] = new MyPoint(4, 5);
        ps[4] = new MyPoint(2, 1);
        ps[5] = new MyPoint(2, 4);

        // ps[0] = new MyPoint(2, 4);
        // ps[1] = new MyPoint(1, 1);
        // ps[2] = new MyPoint(2, 3);
        // ps[3] = new MyPoint(4, 5);
        // ps[4] = new MyPoint(2, 1);
        p.closest(ps);
    }
}
class MyPoint {
    double x;
    double y;
    public MyPoint() {
        this.x = 0;
        this.y = 0;
    }
    public MyPoint(double x, double y) {
        this.x = x;
        this.y = y;
    }
    public String toString(){
        return ("(" + this.x + ", " + this.y + ")");
    }
    public double distance(MyPoint point) {
        double x_diff = Math.abs(this.x - point.x);
        double y_diff = Math.abs(this.y - point.y);

        double hyp = Math.pow(x_diff, 2) + Math.pow(y_diff, 2);
        return Math.sqrt(hyp);
    }
    public void closest(MyPoint[] points) {
        double min_dist = 9999.0;
        int point_index = 0;
        for (int i = 0; i < points.length; i++) {
            double cur_dist = this.distance(points[i]);
            if (cur_dist < min_dist) {
                min_dist = cur_dist;
                point_index = i;
            }
        }
        System.out.println("Closest point to " + this.toString() + " is " + points[point_index].toString() + ". Their distance is " + min_dist + ".");
    }
}