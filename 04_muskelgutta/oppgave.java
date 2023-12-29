import java.util.ArrayList;
import java.util.List;

// Feelings class now contains an array of feelings (strings)
public class Feelings {
    private String[] feelings;

    // Constructor
    public Feelings(String[] feelings) {
        this.feelings = feelings;
    }

    // Getter for feelings array
    public String[] getFeelings() {
        return feelings;
    }

    public static void main(String[] args) {
        Man muscleMan = new Man();
        boolean hasFeelings = muscleMan.insertFeeling("happy");
        if(hasFeelings) {
            System.out.println("MuscleMan has feelings");
        } else {
            System.out.println("MuscleMan has no feelings");
        }
    }
}

// Man class inherits from Feelings
class Man extends Feelings {
    // Constructor accepts an empty array
    public Man() {
        superhero(new String[0]);
    }

    // Public function to receive a feeling and return all feelings
    public boolean insertFeeling(String feeling) {

        return false;
    }
}
