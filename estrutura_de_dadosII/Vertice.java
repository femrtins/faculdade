import java.util.ArrayList;
import java.util.List;

public class Vertice{
    public static int proximoId = 1;
    private int id;
    private String estado;
    private List<Aresta> arestas = new ArrayList<>();
    private List<Aresta> entrada = new ArrayList<>();
    private List<Aresta> saida = new ArrayList<>();


    public Vertice()
    {
        this.id = proximoId++;
    }

    public int getId()
    {
        return id;
    }

    public void addAresta(Aresta e)
    {
        arestas.add(e);
    }

    public void removeAresta(Aresta e)
    {
        arestas.remove(e);
    }

    public void addEntrada(Aresta e)
    {
        entrada.add(e);
    }

    public void addSaida(Aresta e)
    {
        saida.add(e);
    }

    public List<Aresta> listaArestas()
    {
        List<Aresta> lista = new ArrayList<>();
        for(Aresta a: arestas){
            lista.add(a);
        }
        return lista;
    }

    public List<Aresta> listaEntrada()
    {
        List<Aresta> lista = new ArrayList<>();
        for(Aresta a: entrada){
            lista.add(a);
        }
        return lista;
    }

    public List<Aresta> listaSaida()
    {
        List<Aresta> lista = new ArrayList<>();
        for(Aresta a: saida){
            lista.add(a);
        }
        return lista;
    }

    public List<Vertice> adj()
    {
        List<Vertice> lista = new ArrayList<>();
        for (Aresta a: this.listaArestas())
        {
            if (a.getVertice1() == this)
            {
                lista.add(a.getVertice2());
            }
            else
            {
                lista.add(a.getVertice1());
            }
        }

        return lista;
        // int i = 0;
        // System.out.print("<");
        // for (Vertice x : lista)
        // {
        //     System.out.print(x.getId() + (i < lista.size()-1 ? ", " : ""));
        //     i++;
        // }
        // System.out.print(">\n");
    }

    public void setEstado( String a)
    {
        this.estado =  a;
    } 

    public String getEstado()
    {
        return estado;
    } 
}