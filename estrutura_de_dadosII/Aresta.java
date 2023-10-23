public class Aresta{

    public static int proximoId = 1;
    private int id;
    private Vertice v1;
    private Vertice v2;

    public Aresta(Vertice v1, Vertice v2)
    {
        id = proximoId++;
        this.v1 = v1;
        this.v2 = v2;
    }

    public int getId()
    {
        return id;
    }

    public Vertice getVertice1()
    {
        return v1;
    }

    public Vertice getVertice2()
    {
        return v2;
    }
}