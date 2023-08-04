import java.util.Map;
import java.util.HashMap;
import java.awt.Color;
import java.awt.Font;
class Player {
    HashMap<String, Integer> dictionary = new HashMap<String, Integer>();
    protected int score;
    protected int hitBasic;
    protected int hitShrink;
    protected int hitBounce;
    protected int hitSplit;
    protected int hit;
    public Player(int s, HashMap d) {
        int hitBasic = 0;
        int hitShrink = 0;
        int hitBounce = 0;
        int hitSplit = 0;
        int hit = 0;
        score  = 0;
        dictionary = d;
    }
    public int getScore (){
        return score; 
    }
    public Map getInfo(){
        return dictionary;
    }
    public void update(BasicBall ball) {

        if (ball instanceof ShrinkBall){
            hitShrink++;
            hit++;
            score  = score + 20;
            dictionary.put("shrink", hitShrink);
        }
        else if (ball instanceof SplitBall){
            hitSplit++;
            hit++;
            score  = score + 10;
            dictionary.put("split", hitSplit);
        }
        else if (ball instanceof BounceBall){
            hitBounce++;
            hit++;
            score  = score + 15;
            dictionary.put("bounce", hitBounce);
        }
        else if (ball instanceof BasicBall){
            hitBasic++;
            hit++;
            score  = score + 25;
            dictionary.put("basic", hitBasic);
        }
    }
    public void display() {
        StdDraw.setPenColor(StdDraw.YELLOW);
        Font font = new Font("Arial", Font.BOLD, 20);
        StdDraw.setFont(font);
        double i  = 0.05;
        
        StdDraw.text(0, 0.65 - i, "Score: "+ score);
        StdDraw.text(0, 0.6 - i , "basic: "+ dictionary.get("basic"));
        StdDraw.text(0, 0.55 - i , "shrink: "+ dictionary.get("shrink"));
        StdDraw.text(0, 0.5 - i , "bounce: "+ dictionary.get("bounce"));
        StdDraw.text(0, 0.45 - i, "split: "+ dictionary.get("split"));
        StdDraw.show();
        StdDraw.pause(10);  
    }
    public int getHit(){
        return hit;
    }
}
