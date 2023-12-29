# Oppgave

Håndbakhei fra muskelgutta!
Tro det eller ei, men gutta på gymmen driver ikke bare med markløft og sinnsyk cardio.

Vår in-house crossfit-konge Trygve tok seg nemlig et brevkurs i Java i romjula i fjor.

Og gleden stod i taket da det viste seg at han endelig hatt satt i gang med programmet vi gutta har jazza om over en powershake her på bruket.

Endelig skal vi få frem et program hvor du kan teste om du er ekte mann. Fook yeah!

Det er bare et lite problem. Trygve lå nede med en mad lyskestrekk den uka brevet om

arv i Java kom i posten. Så den fikk han aldri studert så nøye.

Og det er litt dritt, fordi nå er det et eller annet ord som er stava feil i koden. Klarer du å finne ut av det? Og gi oss det riktige ordet. Da blir vi skikkelige glade, uten å vise det.

Koden finner dere her:


```java
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
```

# Svar

Kjør `javac oppgave.java`

gir feil
```
oppgave.java:33: error: cannot find symbol
        superhero(new String[0]);
```

```java
superhero(new String[0]);
```

skal være

```java
super(new String[0]);
```

Svar: super
