package brackets;
import java.awt.Canvas;
import java.awt.Color;
import java.awt.Font;
import java.awt.Graphics;
import javax.swing.JFrame;

public class Brackets_Abbaraju {
    private final MyCanvas canvas = new MyCanvas();

    public Brackets_Abbaraju () {
        JFrame frame = new JFrame();
        frame.setSize(1600, 1240);
        frame.setTitle("Pranav Abbaraju - Brackets");
        frame.add(canvas);
        frame.setResizable(false);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);     
    }
    public static void main(String[] args) {
        Brackets_Abbaraju b = new Brackets_Abbaraju();
    }
    

}

class MyCanvas extends Canvas {
    @Override
    public void paint(Graphics g) {
    
        g.setColor(Color.white);
        g.fillRect(0, 0, 1600, 1240);
        
        
        
        g.setColor(new Color(202, 203, 204));
        g.fillRoundRect(240+120+95+95, 563+40, 500, 50, 4, 4);
        g.fillRoundRect(240+35, 160, 1600-(275*2), 55, 4, 4);
        g.fillOval(762, 171, 80, 80);
        
        
        g.setColor(new Color(39, 32, 87));
        g.fillRoundRect(40, 30, 1600 - 80, 60, 4, 4);
        g.setColor(Color.white);
        g.setFont(new Font("Abadi MT Condensed Extra Bold", Font.BOLD + Font.ITALIC, 30));
        g.drawString("2018 NCAA DIVISION I MEN'S BASKETBALL CHAMPIONSHIP BRACKET", 280, 73);
        
        
        g.setFont(new Font("Abadi MT Condensed Extra Bold", Font.BOLD + Font.ITALIC, 16));
        g.setColor(new Color(27, 143, 156));
        g.drawString("FINAL FOUR", 750, 252+25+50+110);
        g.drawString("NATIONAL", 760, 550);
        g.drawString("CHAMPIONSHIP", 738, 567);
        
        
        g.setColor(Color.black);
        g.drawString("FIRST FOUR", 756, 150);
        g.drawString("#MarchMadness", 738, 820);
        g.drawLine(300, 180, 460, 180);
        g.drawLine(460, 180, 460, 206);
        g.drawLine(300, 206, 460, 206);
        g.drawLine(520, 180, 680, 180);
        g.drawLine(680, 180, 680, 206);
        g.drawLine(520, 206, 680, 206);
        
        g.drawLine(920, 180, 1080, 180);
        g.drawLine(920, 180, 920, 206);
        g.drawLine(920, 206, 1080, 206);
        g.drawLine(1140, 180, 1300, 180);
        g.drawLine(1140, 180, 1140, 206);
        g.drawLine(1140, 206, 1300, 206);
        
        
        g.setFont(new Font("Avenir", Font.PLAIN, 11));
        g.drawString("First Round", 45, 105);
        g.drawString("March 15-16", 45, 118);
        g.drawString("Second Round", 245, 105);
        g.drawString("March 17-18", 245, 118);
        g.drawString("Regional", 360, 105);
        g.drawString("Semifinals", 360, 118);
        g.drawString("March 22-23", 360, 131);
        g.drawString("Regional", 455, 105);
        g.drawString("Finals", 455, 118);
        g.drawString("March 24-25", 455, 131);
        g.drawString("National", 550, 105);
        g.drawString("Semifinals", 550, 118);
        g.drawString("March 31", 550, 131);
        g.drawString("First Round", 1500, 105);
        g.drawString("March 15-16", 1495, 118);
        g.drawString("Second Round", 1285, 105);
        g.drawString("March 17-18", 1295, 118);
        g.drawString("Regional", 1190, 105);
        g.drawString("Semifinals", 1185, 118);
        g.drawString("March 22-23", 1175, 131);
        g.drawString("Regional", 1090, 105);
        g.drawString("Finals", 1105, 118);
        g.drawString("March 24-25", 1075, 131);
        g.drawString("National", 990, 105);
        g.drawString("Semifinals", 985, 118);
        g.drawString("March 31", 990, 131);
        g.drawString("March 13-14", 770, 200);
        g.drawString("March 31 and April 2", 753, 252+25+50+110+30);
        g.drawString("April 2", 786, 585);
        
        g.setFont(new Font("Avenir", Font.BOLD, 11));
        g.drawString("DAYTON", 780, 187);
        g.drawString("SAN ANTONIO", 765, 252+25+50+110+15);
        
        
        g.setColor(Color.black);
        g.drawLine(570, 617, 680, 617);
        g.drawLine(570, 638, 680, 638);
        g.drawLine(570, 617, 570, 638);
        g.drawLine(680, 617, 680, 638);
        g.drawLine(920, 617, 1030, 617);
        g.drawLine(920, 638, 1030, 638);
        g.drawLine(920, 617, 920, 638);
        g.drawLine(1030, 617, 1030, 638);
        
        g.drawLine(740, 612, 860, 612);
        g.drawLine(740, 643, 860, 643);
        g.drawLine(740, 612, 740, 643);
        g.drawLine(860, 612, 860, 643);
        
     
        
        
        g.setColor(Color.black);
        g.setFont(new Font("Avenir", Font.PLAIN, 11));
        
        String[] listNum = {"1", "16", "8", "9", "5", "12", "4", "13", "6", "11", "3", "14", "7", "10", "2", "15", "1", "16", "8", "9", "5", "12", "4", "13", "6", "11", "3", "14", "7", "10", "2", "15"};
        
        
        int posx1 = 40;
        int posx2 = 240;
        int posy1 = 240;
        int posy2 = 265;
        int num = posy1 - 2;
        int num2 = posy2 - 2;
        int midpos = posy1 + (posy2 - posy1)/2;
        int newmidpos = midpos + 25;
        int anothermidpos = newmidpos + 50;
        int yetanothermidpos = anothermidpos + 100;
        int posx3 = posx2 + 120;
        int posx4 = posx3 + 95;
        int posx5 = posx4 + 95;
        int posx6 = posx5 + 95;
        
        int a = 0;
        while (a < 32){
            g.drawString(listNum[a], posx1, num);
            g.drawLine(posx1, posy1, posx2, posy1);
            g.drawLine(posx2, posy1, posx2, posy2);
            g.drawString(listNum[a + 1], posx1, num2);
            g.drawLine(posx1, posy2, posx2, posy2);
            posy1+=50;
            posy2+=50;
            num = posy1 - 2;
            num2 = posy2 - 2;
            a += 2;
        }
        int b = 0;
        while (b < 8){
            g.drawLine(posx2, midpos, posx3, midpos);
            g.drawLine(posx3, midpos, posx3, midpos + 50);
            g.drawLine(posx2, midpos + 50, posx3, midpos + 50);
            midpos += 100;
            b += 1;
        }
        int c = 0;
        while (c < 4){
            g.drawLine(posx3, newmidpos, posx4, newmidpos);
            g.drawLine(posx4, newmidpos, posx4, newmidpos + 100);
            g.drawLine(posx3, newmidpos + 100, posx4, newmidpos + 100);
            newmidpos += 200;
            c += 1;
        }
        int d = 0;
        while (d < 2){
            g.drawLine(posx4, anothermidpos, posx5, anothermidpos);
            g.drawLine(posx5, anothermidpos, posx5, anothermidpos + 200);
            g.drawLine(posx4, anothermidpos + 200, posx5, anothermidpos + 200);
            anothermidpos += 400;
            d += 1;
        }
        g.drawLine(posx5, yetanothermidpos, posx6, yetanothermidpos);
        g.drawLine(posx6, yetanothermidpos, posx6, yetanothermidpos + 400);
        g.drawLine(posx5, yetanothermidpos + 400, posx6, yetanothermidpos + 400);
        
        
        
        
        posx1 = 1560;
        posx2 = 1360;
        posy1 = 240;
        posy2 = 265;
        num = posy1 - 2;
        num2 = posy2 - 2;
        midpos = posy1 + (posy2 - posy1)/2;
        newmidpos = midpos + 25;
        anothermidpos = newmidpos + 50;
        yetanothermidpos = anothermidpos + 100;
        posx3 = posx2 - 120;
        posx4 = posx3 - 95;
        posx5 = posx4 - 95;
        posx6 = posx5 - 95;
        
        int e = 0;
        while (e < 32){
            g.drawString(listNum[e], posx1 - 12, num);
            g.drawLine(posx2, posy1, posx1, posy1);
            g.drawLine(posx2, posy1, posx2, posy2);
            g.drawString(listNum[e + 1], posx1 - 12, num2);
            g.drawLine(posx2, posy2, posx1, posy2);
            posy1 += 50;
            posy2 += 50;
            num = posy1 - 2;
            num2 = posy2 - 2;
            e += 2;
        }
        int f = 0;
        while (f < 8){
            g.drawLine(posx3, midpos, posx2, midpos);
            g.drawLine(posx3, midpos, posx3, midpos + 50);
            g.drawLine(posx3, midpos + 50, posx2, midpos + 50);
            midpos += 100;
            f += 1;
        }
        int h = 0;
        while (h < 4){
            g.drawLine(posx4, newmidpos, posx3, newmidpos);
            g.drawLine(posx4, newmidpos, posx4, newmidpos + 100);
            g.drawLine(posx4, newmidpos + 100, posx3, newmidpos + 100);
            newmidpos += 200;
            h += 1;
        }
        int i = 0;
        while (i < 2){
            g.drawLine(posx5, anothermidpos, posx4, anothermidpos);
            g.drawLine(posx5, anothermidpos, posx5, anothermidpos + 200);
            g.drawLine(posx5, anothermidpos + 200, posx4, anothermidpos + 200);
            anothermidpos += 400;
            i += 1;
        }
        g.drawLine(posx6, yetanothermidpos, posx5, yetanothermidpos);
        g.drawLine(posx6, yetanothermidpos, posx6, yetanothermidpos + 400);
        g.drawLine(posx6, yetanothermidpos + 400, posx5, yetanothermidpos + 400);
        
        

        g.setColor(Color.white);
        g.fillRect(571, 618, 109, 20);
        g.fillRect(921, 618, 109, 20);
        g.fillRect(741, 613, 119, 30);
        
           
    } 
}