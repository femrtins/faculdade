import java.util.ArrayList;
import java.util.List;

public class Fila {
    private List<Vertice> fila = new ArrayList<>();

    public void insere(Vertice e)
    {
        fila.add(e);
    }

    public Vertice remove()
    {
        Vertice a = fila.remove(0);
        return a;    
    }
}
