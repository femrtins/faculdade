import java.util.ArrayList;

public class GrafoDirigido extends Grafo {

    private ArrayList<Aresta> arestas = new ArrayList<>();

    public GrafoDirigido()
    {
    }

    public Aresta insereA(Vertice v, Vertice u)
    {
        Aresta a = new Aresta(v, u);
        v.addEntrada(a);
        u.addSaida(a);
        v.addAresta(a);
        u.addAresta(a);
        arestas.add(a);
        return a;
    }

    public Aresta getA(Vertice v, Vertice u)
    {
        for (Aresta a : v.listaEntrada())
        {
            for (Aresta b : u.listaSaida())
            {
                if(a == b){ return a; }                
            }
        }
        return null;
    }

    public int grauE(Vertice v)
    {
        return v.listaEntrada().size();
    }

    public int grauS(Vertice v)
    {
        return v.listaSaida().size();
    }

    public void arestasE(Vertice v)
    {
        int i = 0;
        System.out.print("<");
        for (Aresta a : v.listaEntrada())
        {
            System.out.print(a.getId() + (i < v.listaEntrada().size()-1 ? ", " : ""));
            i++;
        }
        System.out.print(">\n");
    }

        

    public void arestasS(Vertice v)
    {
        int i = 0;
        System.out.print("<");
        for (Aresta a : v.listaSaida())
        {
            System.out.print(a.getId() + (i < v.listaSaida().size()-1 ? ", " : ""));
            i++;
        }
        System.out.print(">\n");
    }

    @Override
    public String toString()
    {
        String x = new String();
        for (Aresta a: arestas)
        {
            x += (a.getVertice1().getId() + " ──> " + a.getVertice2().getId() + "\n");
        }
        return x;
    }

}
