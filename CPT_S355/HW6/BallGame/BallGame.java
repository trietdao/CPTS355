/******************************************************************************
 *  Compilation:  javac BallGame.java
 *  Execution:    java BallGame n
 *  Dependencies: BasicBall.java StdDraw.java
 *
 *  Creates a BasicBall and animates it
 *
 *  Part of the animation code is adapted from Computer Science:   An Interdisciplinary Approach Book
 *  
 *  Run the skeleton code with arguments : 1  basic  0.08
 *******************************************************************************/
import java.awt.Color;
import java.awt.Font;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
public class BallGame { 

    public static void main(String[] args) {
  
    	// number of bouncing balls
    	int numBalls = Integer.parseInt(args[0]);
    	//ball types
    	String ballTypes[] = new String[numBalls];
    	//sizes of balls
    	double ballSizes[] = new double[numBalls];
    	HashMap<String, Integer> dictionary = new HashMap<>();
        dictionary.put("basic", 0);
        dictionary.put("bounce", 0);
        dictionary.put("shrink", 0);
        dictionary.put("split", 0);
    	//retrieve ball types
    	int index =1;
    	for (int i=0; i<numBalls; i++) {
    		ballTypes[i] = args[index];
    		index = index+2;
    	}
    	//retrieve ball sizes
    	index = 2;
    	for (int i=0; i<numBalls; i++) {
    		ballSizes[i] = Double.parseDouble(args[index]);
    		index = index+2;
    	}
        
    	//TO DO: create a Player object and initialize the player game stats.  
    	Player result = new Player(0,dictionary);

    	//number of active balls
    	int numBallsinGame = 0;
        StdDraw.enableDoubleBuffering();

        StdDraw.setCanvasSize(800, 800);
        // set boundary to box with coordinates between -1 and +1
        StdDraw.setXscale(-1.0, +1.0);
        StdDraw.setYscale(-1.0, +1.0);

        // create colored balls 
        //TO DO: Create "numBalls" balls (of types given in "ballTypes" with sizes given in "ballSizes") and store them in an Arraylist
   		//BasicBall ball = new BasicBall(ballSizes[0],Color.RED);
        ArrayList<BasicBall> ballList = new ArrayList<BasicBall>();
        ArrayList<SplitBall> holdList = new ArrayList<SplitBall>();
        for (int i = 0; i < numBalls; i++){
            String basic = "basic";
            String shrink = "shrink";
            String bounce = "bounce";
            String split = "split";
            if (ballTypes[i].equalsIgnoreCase(basic)){
                BasicBall ball = new BasicBall(ballSizes[i],Color.BLACK);
                ballList.add(ball);
            }
            else if (ballTypes[i].equalsIgnoreCase(shrink)){
                BasicBall ball = new ShrinkBall(ballSizes[i],Color.RED);
                ballList.add(ball);
            }
            else if (ballTypes[i].equalsIgnoreCase(bounce)){
                BasicBall ball = new BounceBall(ballSizes[i],Color.BLUE);
                ballList.add(ball);       
            }
            else if (ballTypes[i].equalsIgnoreCase(split)){
                BasicBall ball = new SplitBall(ballSizes[i],Color.YELLOW);
                ballList.add(ball);       
            }
        }
   		//TO DO: initialize the numBallsinGame
   		numBallsinGame++;

        // do the animation loop
        StdDraw.enableDoubleBuffering();
        while (numBallsinGame > 0) {

        	// TODO: move all balls
            for (BasicBall ball : ballList){
                ball.move();
            }
            //Check if the mouse is clicked
            if (StdDraw.isMousePressed()) {
                double x = StdDraw.mouseX();
                double y = StdDraw.mouseY();
                //TODO: check whether a ball is hit. Check each ball.  
                for (BasicBall ball : ballList){
                    if (ball.isHit(x,y)) {
                            result.update(ball);
                            ball.reset();
                            
                            if (ball instanceof SplitBall){
                                holdList.add(new SplitBall(ball.getRadius(), Color.YELLOW));
                            }
                    }
                }
            }
            for (SplitBall ball : holdList){
                ballList.add(ball);
            }   
            holdList.clear(); 
            numBallsinGame= 0;
            // draw the n balls
            StdDraw.clear(StdDraw.GRAY);
            StdDraw.setPenColor(StdDraw.BLACK);
            
            //TO DO: check each ball and see if they are still visible. numBallsinGame should hold the number of visible balls in the game. 
            for (BasicBall ball : ballList){ 
                if (ball.isOut == false) { 
                    ball.draw();
                    numBallsinGame++;
                }
            }
            //Print the game progress
            StdDraw.setPenColor(StdDraw.YELLOW);
            Font font = new Font("Arial", Font.PLAIN, 20);
            StdDraw.setFont(font);
            StdDraw.text(-0.65, 0.90, "Number of balls in game: "+ String.valueOf(numBallsinGame));
            StdDraw.text(-0.65, 0.85, "Number of hits: "+ String.valueOf(result.getHit()));
            StdDraw.text(-0.65, 0.8, "Score: "+ String.valueOf(result.getScore()));
            StdDraw.show();
            StdDraw.pause(20);
        }
        while (true) {
            StdDraw.setPenColor(StdDraw.BLUE);
            Font font = new Font("Arial", Font.BOLD, 60);
            StdDraw.setFont(font);
            StdDraw.text(0, 0.7, "GAME OVER");
            //TO DO: print the rest of the player statistics
            result.display();
            StdDraw.show();
            StdDraw.pause(10);           
        }
        	
        
    }
}
