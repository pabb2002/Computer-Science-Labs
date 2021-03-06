import java.awt.Canvas;
import java.awt.Color;
import java.awt.Font;
import java.awt.Graphics;

import javax.swing.JFrame;

public class SimpsonsHouse_Abbaraju {
	private final HouseCanvas canvas = new HouseCanvas();
	
	public SimpsonsHouse_Abbaraju() {
		JFrame frame = new JFrame();
		frame.setSize(946,845);
		frame.setTitle("Pranav Abbaraju - Simpson's House");
		frame.add(canvas);
		frame.setResizable(false);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.setVisible(true);
	}
	
	public static void main(String[] args) {
		SimpsonsHouse_Abbaraju house = new SimpsonsHouse_Abbaraju();
	}

}

class HouseCanvas extends Canvas {
        @Override
	public void paint(Graphics g) {
                //background
		g.setColor(new Color(196, 212, 228));
		g.fillRect(0, 0, 946, 845);
                g.setColor(new Color(1, 168, 122));
                g.fillRect(0, 546, 946, 845-546);
		
                //main front of house
                g.setColor(Color.black);
                g.fillRect(77, 265, 623-77, 573-265);
                g.setColor(new Color(255, 172, 111));
                g.fillRect(80, 265, 620-80, 570-264);
                //top windows
                g.setColor(Color.black);
                g.fillRect(130, 263, 262-130, 308-263);
		g.fillRect(441, 263, 570-441, 308-263);
                g.setColor(new Color(147, 241, 215));
                g.fillRect(140, 263, 190-140, 305-263);
                g.fillRect(200, 263, 259-200, 305-263);
                g.fillRect(444, 263, 500-444, 305-263);
                g.fillRect(510, 263, 560-510, 305-263);
                g.setColor(new Color(107, 72, 30));
                g.fillRect(132, 263, 6, 305-263);
		g.fillRect(192, 263, 6, 305-263);
                g.fillRect(502, 263, 6, 305-263);
		g.fillRect(562, 263, 6, 305-263);
                g.setColor(new Color(49, 83, 77));
                g.setFont(new Font("Apple Chancery", Font.ITALIC + Font.BOLD, 20));
                g.drawString("/", 155, 293);
                g.drawString("/", 219, 289);
                g.drawString("/", 460, 291);
                g.drawString("/", 525, 293);
                g.setColor(new Color(84, 141, 132));
                g.setFont(new Font("Apple Chancery", Font.ITALIC + Font.BOLD, 16));
                g.drawString("/", 160, 297);
                g.drawString("/", 224, 293);
                g.drawString("/", 465, 295);
                g.drawString("/", 530, 297);
                //left windows
                g.setColor(Color.black);
                g.fillOval(119, 367, 261-119, 120);
                g.setColor(new Color(107, 72, 30));
                g.fillOval(120, 369, 261-121, 118);
                g.setColor(Color.black);
                int[] xPointsLeftWindowsBlack = {118, 118, 131, 240, 262, 262, 241, 135};
                int[] yPointsLeftWindowsBlack = {540, 420, 415, 415, 420, 540, 545, 546};
                g.fillPolygon(xPointsLeftWindowsBlack, yPointsLeftWindowsBlack, 8);
                g.setColor(new Color(147, 241, 215));
                int[] xPointsLeftWindow1 = {120, 120, 125, 125};
                int[] yPointsLeftWindow1 = {459, 423, 421, 457};
                g.fillPolygon(xPointsLeftWindow1, yPointsLeftWindow1, 4);
                int[] xPointsLeftWindow2 = {120, 120, 125, 125};
                int[] yPointsLeftWindow2 = {495, 464, 462, 495};
                g.fillPolygon(xPointsLeftWindow2, yPointsLeftWindow2, 4);
                int[] xPointsLeftWindow3 = {120, 120, 125, 125};
                int[] yPointsLeftWindow3 = {528, 499, 498, 530};
                g.fillPolygon(xPointsLeftWindow3, yPointsLeftWindow3, 4);
                int[] xPointsLeftWindow4 = {127, 127, 132, 132};
                int[] yPointsLeftWindow4 = {456, 420, 418, 453};
                g.fillPolygon(xPointsLeftWindow4, yPointsLeftWindow4, 4);
                int[] xPointsLeftWindow5 = {127, 127, 132, 132};
                int[] yPointsLeftWindow5 = {495, 461, 459, 494};
                g.fillPolygon(xPointsLeftWindow5, yPointsLeftWindow5, 4);
                int[] xPointsLeftWindow6 = {127, 127, 132, 132};
                int[] yPointsLeftWindow6 = {530, 498, 497, 532};
                g.fillPolygon(xPointsLeftWindow6, yPointsLeftWindow6, 4);
                int[] xPointsLeftWindow7 = {135, 135, 185, 185};
                int[] yPointsLeftWindow7 = {453, 418, 418, 453};
                g.fillPolygon(xPointsLeftWindow7, yPointsLeftWindow7, 4);
                int[] xPointsLeftWindow8 = {135, 135, 185, 185};
                int[] yPointsLeftWindow8 = {494, 458, 458, 494};
                g.fillPolygon(xPointsLeftWindow8, yPointsLeftWindow8, 4);
                int[] xPointsLeftWindow9 = {135, 135, 185, 185};
                int[] yPointsLeftWindow9 = {532, 498, 498, 532};
                g.fillPolygon(xPointsLeftWindow9, yPointsLeftWindow9, 4);
                int[] xPointsLeftWindow10 = {189, 189, 239, 239};
                int[] yPointsLeftWindow10 = {453, 418, 418, 453};
                g.fillPolygon(xPointsLeftWindow10, yPointsLeftWindow10, 4);
                int[] xPointsLeftWindow11 = {189, 189, 239, 239};
                int[] yPointsLeftWindow11 = {494, 458, 458, 494};
                g.fillPolygon(xPointsLeftWindow11, yPointsLeftWindow11, 4);
                int[] xPointsLeftWindow12 = {189, 189, 239, 239};
                int[] yPointsLeftWindow12 = {532, 498, 498, 532};
                g.fillPolygon(xPointsLeftWindow12, yPointsLeftWindow12, 4);
                int[] xPointsLeftWindow13 = {242, 242, 249, 249};
                int[] yPointsLeftWindow13 = {453, 418, 420, 456};
                g.fillPolygon(xPointsLeftWindow13, yPointsLeftWindow13, 4);
                int[] xPointsLeftWindow14 = {242, 242, 249, 249};
                int[] yPointsLeftWindow14 = {493, 458, 461, 494};
                g.fillPolygon(xPointsLeftWindow14, yPointsLeftWindow14, 4);
                int[] xPointsLeftWindow15 = {242, 242, 249, 249};
                int[] yPointsLeftWindow15 = {531, 496, 497, 529};
                g.fillPolygon(xPointsLeftWindow15, yPointsLeftWindow15, 4);
                int[] xPointsLeftWindow16 = {252, 252, 259, 259};
                int[] yPointsLeftWindow16 = {456, 420, 423, 459};
                g.fillPolygon(xPointsLeftWindow16, yPointsLeftWindow16, 4);
                int[] xPointsLeftWindow17 = {252, 252, 259, 259};
                int[] yPointsLeftWindow17 = {493, 461, 464, 494};
                g.fillPolygon(xPointsLeftWindow17, yPointsLeftWindow17, 4);
                int[] xPointsLeftWindow18 = {252, 252, 259, 259};
                int[] yPointsLeftWindow18 = {530, 497, 498, 528};
                g.fillPolygon(xPointsLeftWindow18, yPointsLeftWindow18, 4);
                g.setColor(new Color(107, 72, 30));
                int[] xPointsLeftWindowBottom1 = {120, 120, 132, 132};
                int[] yPointsLeftWindowBottom1 = {538, 531, 535, 542};
                g.fillPolygon(xPointsLeftWindowBottom1, yPointsLeftWindowBottom1, 4);
                int[] xPointsLeftWindowBottom2 = {135, 135, 239, 239};
                int[] yPointsLeftWindowBottom2 = {543, 535, 535, 543};
                g.fillPolygon(xPointsLeftWindowBottom2, yPointsLeftWindowBottom2, 4);
                int[] xPointsLeftWindowBottom3 = {241, 241, 260, 260};
                int[] yPointsLeftWindowBottom3 = {542, 534, 531, 538};
                g.fillPolygon(xPointsLeftWindowBottom3, yPointsLeftWindowBottom3, 4);
                //right windows
                g.setColor(Color.black);
                g.fillOval(442, 367, 261-119, 120);
                g.setColor(new Color(107, 72, 30));
                g.fillOval(443, 369, 261-121, 118);
                g.setColor(Color.black);
                int[] xPointsRightWindowsBlack = {442, 442, 457, 570, 586, 586, 567, 460};
                int[] yPointsRightWindowsBlack = {540, 420, 415, 415, 420, 540, 545, 546};
                g.fillPolygon(xPointsRightWindowsBlack, yPointsRightWindowsBlack, 8);
                g.setColor(new Color(147, 241, 215));
                int[] xPointsRightWindow1 = {444, 444, 449, 449};
                int[] yPointsRightWindow1 = {459, 423, 421, 457};
                g.fillPolygon(xPointsRightWindow1, yPointsRightWindow1, 4);
                int[] xPointsRightWindow2 = {444, 444, 449, 449};
                int[] yPointsRightWindow2 = {495, 464, 462, 495};
                g.fillPolygon(xPointsRightWindow2, yPointsRightWindow2, 4);
                int[] xPointsRightWindow3 = {444, 444, 449, 449};
                int[] yPointsRightWindow3 = {528, 499, 498, 530};
                g.fillPolygon(xPointsRightWindow3, yPointsRightWindow3, 4);
                int[] xPointsRightWindow4 = {451, 451, 456, 456};
                int[] yPointsRightWindow4 = {456, 420, 418, 453};
                g.fillPolygon(xPointsRightWindow4, yPointsRightWindow4, 4);
                int[] xPointsRightWindow5 = {451, 451, 456, 456};
                int[] yPointsRightWindow5 = {495, 461, 459, 494};
                g.fillPolygon(xPointsRightWindow5, yPointsRightWindow5, 4);
                int[] xPointsRightWindow6 = {451, 451, 456, 456};
                int[] yPointsRightWindow6 = {530, 498, 497, 532};
                g.fillPolygon(xPointsRightWindow6, yPointsRightWindow6, 4);
                int[] xPointsRightWindow7 = {459, 459, 509, 509};
                int[] yPointsRightWindow7 = {453, 418, 418, 453};
                g.fillPolygon(xPointsRightWindow7, yPointsRightWindow7, 4);
                int[] xPointsRightWindow8 = {459, 459, 509, 509};
                int[] yPointsRightWindow8 = {494, 458, 458, 494};
                g.fillPolygon(xPointsRightWindow8, yPointsRightWindow8, 4);
                int[] xPointsRightWindow9 = {459, 459, 509, 509};
                int[] yPointsRightWindow9 = {532, 498, 498, 532};
                g.fillPolygon(xPointsRightWindow9, yPointsRightWindow9, 4);
                int[] xPointsRightWindow10 = {513, 513, 563, 563};
                int[] yPointsRightWindow10 = {453, 418, 418, 453};
                g.fillPolygon(xPointsRightWindow10, yPointsRightWindow10, 4);
                int[] xPointsRightWindow11 = {513, 513, 563, 563};
                int[] yPointsRightWindow11 = {494, 458, 458, 494};
                g.fillPolygon(xPointsRightWindow11, yPointsRightWindow11, 4);
                int[] xPointsRightWindow12 = {513, 513, 563, 563};
                int[] yPointsRightWindow12 = {532, 498, 498, 532};
                g.fillPolygon(xPointsRightWindow12, yPointsRightWindow12, 4);
                int[] xPointsRightWindow13 = {566, 566, 573, 573};
                int[] yPointsRightWindow13 = {453, 418, 420, 456};
                g.fillPolygon(xPointsRightWindow13, yPointsRightWindow13, 4);
                int[] xPointsRightWindow14 = {566, 566, 573, 573};
                int[] yPointsRightWindow14 = {493, 458, 461, 494};
                g.fillPolygon(xPointsRightWindow14, yPointsRightWindow14, 4);
                int[] xPointsRightWindow15 = {566, 566, 573, 573};
                int[] yPointsRightWindow15 = {531, 496, 497, 529};
                g.fillPolygon(xPointsRightWindow15, yPointsRightWindow15, 4);
                int[] xPointsRightWindow16 = {576, 576, 583, 583};
                int[] yPointsRightWindow16 = {456, 420, 423, 459};
                g.fillPolygon(xPointsRightWindow16, yPointsRightWindow16, 4);
                int[] xPointsRightWindow17 = {576, 576, 583, 583};
                int[] yPointsRightWindow17 = {493, 461, 464, 494};
                g.fillPolygon(xPointsRightWindow17, yPointsRightWindow17, 4);
                int[] xPointsRightWindow18 = {576, 576, 583, 583};
                int[] yPointsRightWindow18 = {530, 497, 498, 528};
                g.fillPolygon(xPointsRightWindow18, yPointsRightWindow18, 4);
                g.setColor(new Color(107, 72, 30));
                int[] xPointsRightWindowBottom1 = {444, 444, 456, 456};
                int[] yPointsRightWindowBottom1 = {538, 531, 535, 542};
                g.fillPolygon(xPointsRightWindowBottom1, yPointsRightWindowBottom1, 4);
                int[] xPointsRightWindowBottom2 = {459, 459, 563, 563};
                int[] yPointsRightWindowBottom2 = {543, 535, 535, 543};
                g.fillPolygon(xPointsRightWindowBottom2, yPointsRightWindowBottom2, 4);
                int[] xPointsRightWindowBottom3 = {565, 565, 584, 584};
                int[] yPointsRightWindowBottom3 = {542, 534, 531, 538};
                g.fillPolygon(xPointsRightWindowBottom3, yPointsRightWindowBottom3, 4);
                //door
                g.setColor(Color.black);
                g.fillOval(290, 375, 120, 120);
                g.fillRect(291, 437, 120, 135);
                g.setColor(new Color(107, 72, 30));
                g.fillRoundRect(296, 410, 110, 100, 40, 40);
                g.fillRect(296, 445, 110, 127);
                g.fillOval(302, 382, 97, 120);
                g.setColor(Color.black);
                g.fillRoundRect(310, 407, 387-307, 560-407, 30, 30);
                g.fillRoundRect(310, 420, 80, 140, 20, 20);
                g.setColor(new Color(248, 165, 159));
                g.fillRoundRect(313, 410, 387-313, 557-411, 40, 40);
                g.fillRoundRect(313, 420, 387-313, 557-420, 20, 20);
                g.setColor(Color.black);
                g.fillOval(343, 440, 12, 12);
                g.fillOval(345, 450, 8, 8);
                g.fillOval(311, 500, 12, 12);
                g.fillOval(393, 505, 12, 13);
                g.setColor(new Color(69, 69, 215));
                g.fillOval(312, 501, 10, 10);
                g.setColor(new Color(169, 193, 195));
                g.fillOval(344, 441, 10, 10);
                g.fillOval(347, 451, 6, 6);
                g.setColor(Color.black);
                g.fillOval(345, 442, 8, 9);
                g.fillRect(348, 450, 2, 5);
                g.setColor(new Color(169, 193, 195));
                g.fillOval(345, 443, 6, 7);
                g.setColor(new Color(37, 45, 91));
                g.fillOval(394, 506, 10, 11);
                g.setColor(Color.black);
                g.fillOval(397, 508, 6, 7);
                //pathway
                g.setColor(Color.black);
                int[] xPointsPathwayBlack = {285, 296, 296};
                int[] yPointsPathwayBlack = {639, 591, 289};
                g.fillPolygon(xPointsPathwayBlack, yPointsPathwayBlack, 12);
                //main roof
                g.setColor(Color.black);
                g.fillRect(66, 247, 640-66, 264-247);
                g.fillRect(60, 238, 647-60, 250-238);
                int[] xPointsRoofBlack = {133, 570, 647, 59};
                int[] yPointsRoofBlack = {142, 142, 238, 238};
                g.fillPolygon(xPointsRoofBlack, yPointsRoofBlack, 4);
                g.setColor(new Color(107, 72, 30));
                int[] xPointsRoofBrown = {135, 569, 642, 63};
                int[] yPointsRoofBrown = {145, 145, 238, 238};
                g.fillPolygon(xPointsRoofBrown, yPointsRoofBrown, 4);
                g.fillRect(69, 250, 637-69, 261-250);
                g.fillRect(63, 241, 644-63, 247-241);
                
                //garage black
                g.setColor(Color.black);
                int[] xPointsGarageBlack = {637, 620, 620, 731, 775, 907, 906, 874, 874};
                int[] yPointsGarageBlack = {597, 577, 400, 335, 324, 404, 416, 416, 597};
                g.fillPolygon(xPointsGarageBlack, yPointsGarageBlack, 9);
                //garage tan
                g.setColor(new Color(255, 172, 111));
                int[] xPointsGarageFront = {640, 640, 760, 760, 767, 779, 779, 871, 871};
                int[] yPointsGarageFront = {594, 413, 345, 370, 370, 362, 355, 409, 593};
                g.fillPolygon(xPointsGarageFront, yPointsGarageFront, 9);
                int[] xPointsGarageSide = {637, 623, 623, 637};
                int[] yPointsGarageSide = {594, 577, 415, 415};
                g.fillPolygon(xPointsGarageSide, yPointsGarageSide, 4);
                //garage roof
                g.setColor(new Color(107, 72, 30));
                int[] xPointsGarageRoof1 = {623, 623, 640, 640};
                int[] yPointsGarageRoof1 = {412, 407, 406, 411};
                g.fillPolygon(xPointsGarageRoof1, yPointsGarageRoof1, 4);
                int[] xPointsGarageRoof2 = {622, 733, 763, 640};
                int[] yPointsGarageRoof2 = {403, 339, 331, 402};
                g.fillPolygon(xPointsGarageRoof2, yPointsGarageRoof2, 4);
                int[] xPointsGarageRoof3 = {642, 642, 775, 905, 905, 775};
                int[] yPointsGarageRoof3 = {410, 404, 329, 406, 411, 332};
                g.fillPolygon(xPointsGarageRoof3, yPointsGarageRoof3, 6);
                g.setColor(new Color(75, 55, 31));
                int[] xPointsGarageRoof4 = {875, 875, 779, 779, 903};
                int[] yPointsGarageRoof4 = {413, 407, 352, 337, 413};
                g.fillPolygon(xPointsGarageRoof4, yPointsGarageRoof4, 5);
                int[] xPointsGarageRoof5 = {763, 763, 765, 765, 769, 769, 775, 775, 767};
                int[] yPointsGarageRoof5 = {367, 345, 342, 360, 360, 342, 337, 360, 367};
                g.fillPolygon(xPointsGarageRoof5, yPointsGarageRoof5, 9);
                //garage window
                g.setColor(Color.black);
                g.fillRect(750, 385, 785-750, 419-388);
                g.setColor(new Color(107, 72, 30));
                int[] xPointsGarageWindow = {750, 782, 782, 779, 779, 750};
                int[] yPointsGarageWindow = {387, 387, 416, 416, 390, 390};
                g.fillPolygon(xPointsGarageWindow, yPointsGarageWindow, 6);
                g.setColor(new Color(147, 241, 215));
                g.fillRect(752, 392, 11, 10);
                g.fillRect(765, 392, 11, 10);
                g.fillRect(752, 404, 11, 10);
                g.fillRect(765, 404, 11, 10);
                //garagedoor
                g.setColor(Color.black);
                g.fillRect(663, 438, 855-663, 595-438);
                g.setColor(new Color(107, 72, 30));
                int[] xPointsGarageDoorBrown1 = {666, 666, 668, 668};
                int[] yPointsGarageDoorBrown1 = {444, 440, 440, 444};
                g.fillPolygon(xPointsGarageDoorBrown1, yPointsGarageDoorBrown1, 4);
                int[] xPointsGarageDoorBrown2 = {670, 670, 846, 846};
                int[] yPointsGarageDoorBrown2 = {444, 440, 440, 444};
                g.fillPolygon(xPointsGarageDoorBrown2, yPointsGarageDoorBrown2, 4);
                int[] xPointsGarageDoorBrown3 = {848, 848, 852, 852};
                int[] yPointsGarageDoorBrown3 = {444, 440, 440, 444};
                g.fillPolygon(xPointsGarageDoorBrown3, yPointsGarageDoorBrown3, 4);
                int[] xPointsGarageDoorBrown4 = {848, 848, 852, 852};
                int[] yPointsGarageDoorBrown4 = {593, 447, 447, 593};
                g.fillPolygon(xPointsGarageDoorBrown4, yPointsGarageDoorBrown4, 4);
                int[] xPointsGarageDoorBrown5 = {666, 666, 668, 668};
                int[] yPointsGarageDoorBrown5 = {593, 447, 447, 593};
                g.fillPolygon(xPointsGarageDoorBrown5, yPointsGarageDoorBrown5, 4);
                g.setColor(new Color(231, 173, 127));
                int[] xPointsGarageDoorTan1 = {670, 670, 846, 846};
                int[] yPointsGarageDoorTan1 = {487, 447, 447, 487};
                g.fillPolygon(xPointsGarageDoorTan1, yPointsGarageDoorTan1, 4);
                int[] xPointsGarageDoorTan2 = {670, 670, 846, 846};
                int[] yPointsGarageDoorTan2 = {543, 490, 490, 543};
                g.fillPolygon(xPointsGarageDoorTan2, yPointsGarageDoorTan2, 4);
                int[] xPointsGarageDoorTan3 = {670, 670, 846, 846};
                int[] yPointsGarageDoorTan3 = {593, 546, 546, 593};
                g.fillPolygon(xPointsGarageDoorTan3, yPointsGarageDoorTan3, 4);
                
                
                //back black
                g.setColor(Color.black);
                int[] xPointsBackBlack = {622, 622, 640, 640, 645, 645, 620, 759, 815, 815, 810, 810, 801, 801, 774, 731};
                int[] yPointsBackBlack = {400, 262, 262, 250, 250, 240, 210, 210, 280, 290, 290, 300, 300, 344, 325, 335};
                g.fillPolygon(xPointsBackBlack, yPointsBackBlack, 16);
                //back tan
                g.setColor(new Color(255, 172, 111));
                int[] xPointsBackFront = {623, 623, 798, 798, 774, 731};
                int[] yPointsBackFront = {397, 300, 300, 338, 325, 335};
                g.fillPolygon(xPointsBackFront, yPointsBackFront, 6);
                //back roof
                g.setColor(new Color(107, 72, 30));
                int[] xPointsBackRoof1 = {623, 623, 641, 641, 647, 647, 626, 756, 810};
                int[] yPointsBackRoof1 = {279, 264, 264, 251, 251, 240, 213, 213, 279};
                g.fillPolygon(xPointsBackRoof1, yPointsBackRoof1, 9);
                g.fillRect(623, 282, 812-623, 5);
                //back windows
                g.setColor(new Color(75, 55, 31));
                g.fillRect(623, 290, 807-623, 7);
                g.setColor(Color.black);
                g.fillRect(647, 300, 740-647, 337-300);
                g.setColor(new Color(147, 241, 215));
                g.fillRect(650, 300, 685-650, 334-300);
                g.fillRect(693, 300, 730-693, 334-300);
                g.setColor(new Color(107, 72, 30));
                g.fillRect(687, 300, 3, 334-300);
                g.fillRect(733, 300, 5, 334-300);
                g.setFont(new Font("Apple Chancery", Font.ITALIC + Font.BOLD, 20));
                g.drawString("/", 660, 323);
                g.drawString("/", 706, 323);
                g.setFont(new Font("Apple Chancery", Font.ITALIC + Font.BOLD, 16));
                g.drawString("/", 665, 327);
                g.drawString("/", 711, 327);
                
	}
}