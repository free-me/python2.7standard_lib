import java.io.*;

public class ReadTextFile {
    public static void main(String args[]) {
        int num = 0;
        try {
            FileReader fr = new FileReader("C:\\Users\\MENGL\\IdeaProjects\\PythonStandardLib2.7\\count_code\\src\\111.txt");
            BufferedReader br = new BufferedReader(fr);
            String s = br.readLine();
            while (s != null) {
                if(s.indexOf("no more than 5 messages") ==-1)
                { num =num + 1;
                    System.out.println(num+s);}
                else if( s.indexOf("代码行定位") != -1)
                    System.out.println(s);
                s = br.readLine();
            }
            File dfi = new File("C:\\\\Users\\\\MENGL\\\\IdeaProjects\\\\PythonStandardLib2.7\\\\count_code\\\\src\\\\111.txt");
        }catch (IOException e)
        {
            System.out.println(e);
        }
    }
}
