/******************************************************************************
 *  Compilation:  javac ColoredBall.java
 *  Execution:    java ColoredBall
 *  Dependencies: StdDraw.java
 *
 *  Implementation of a 2-d ball moving in square with coordinates
 *  between -1 and +1. Bounces off the walls upon collision.
 *  
 *
 ******************************************************************************/

import java.awt.Color;

public class BasicBall { 
    protected double rx, ry;         // position
    protected double vx, vy;         // velocity
    protected double radius;   // radius
    protected final Color color;     // color
    public boolean isOut;
    

    // constructor
    public BasicBall(double r, Color c) {
        rx = 0.0;
        ry = 0.0;
        vx = StdRandom.uniform(-0.01, 0.01);
        vy = StdRandom.uniform(-0.01, 0.01);
        radius = r;
        color = c;
        isOut = false;
    }
   
   
    // move the ball one step
    public void move() {
        rx = rx + vx;
        ry = ry + vy;
        if ((Math.abs(rx) > 1.0) || (Math.abs(ry) > 1.0)) 
        	isOut = true;
    }

    // draw the ball
    public void draw() { 
    	if ((Math.abs(rx) <= 1.0) && (Math.abs(ry) <= 1.0)) {
    		StdDraw.setPenColor(color);
    		StdDraw.filledCircle(rx, ry, radius);
    	} else
    		isOut = true;
    	
    }

    public int reset() {
        vx = StdRandom.uniform(-0.01, 0.01);
        vy = StdRandom.uniform(-0.01, 0.01);
        rx = 0.0 ;
        ry = 0.0 ;  	
        // TO DO: assign a random speed 
        return 1;
    }
    
    public boolean isHit(double x, double y) {
    	if ((Math.abs(rx-x)<=radius) && (Math.abs(ry-y)<=radius))
			return true;
		else return false; 
    }
    public int getScore() {
    	return 25;
    }
    
    public double getRadius() {
    	return radius;
    }
}
    class BounceBall extends BasicBall {
        int bounce_count = 3;
        public BounceBall (double r, Color c){
            super(r, c);
        }
        public void move() {
            rx = rx + vx;
            ry = ry + vy;
            if ((Math.abs(rx) >= (1.0 - radius))) {
                bounce_count--;
                if (bounce_count == 0){
                    isOut = true;
                }
                vx = -vx;
            }
            else if ((Math.abs(ry) >= (1.0 - radius))){
                bounce_count--;
                if (bounce_count == 0){
                    isOut = true;
                }
                vy = -vy;
            }
        }
        public int getScore() {
            return 15;
        }
    
    }
    class SplitBall extends BasicBall{
        public SplitBall(double r, Color c){
            super(r,c);
        }
    }
    class ShrinkBall extends BasicBall {
        double input_radius = radius; 
    
        public ShrinkBall (double r, Color c){
            super(r,c);
        }
        public int reset() {
            vx = StdRandom.uniform(-0.01, 0.01);
            vy = StdRandom.uniform(-0.01, 0.01);
            rx = 0.0 ;
            ry = 0.0 ; 
            if (radius <= input_radius * 0.25){
                radius = input_radius;
            } 
            else{
                radius = radius * 2/3;
            }
            return 1;
        }
        public int getScore() {
            return 20;
        }
    }

