import javax.swing.*;
import java.awt.*;
import java.awt.geom.*;

public class AnimatedDragon extends JPanel {
    private double t = 0;

    public AnimatedDragon() {
        setPreferredSize(new Dimension(800, 600));
        setBackground(new Color(20, 26, 45));

        new Timer(30, e -> {
            t += 0.08;
            repaint();
        }).start();
    }

    @Override
    protected void paintComponent(Graphics graphics) {
        super.paintComponent(graphics);
        Graphics2D g = (Graphics2D) graphics.create();
        g.setRenderingHint(RenderingHints.KEY_ANTIALIASING,
                           RenderingHints.VALUE_ANTIALIAS_ON);

        // Gentle floating motion
        double bob = Math.sin(t) * 12;
        g.translate(0, bob);

        drawTail(g);
        drawWings(g);
        drawBody(g);
        drawHead(g);
        drawFire(g);

        g.dispose();
    }

    private void drawBody(Graphics2D g) {
        // Body
        g.setColor(new Color(40, 190, 115));
        g.fill(new Ellipse2D.Double(270, 300, 260, 120));

        // Belly
        g.setColor(new Color(180, 220, 100));
        g.fill(new Ellipse2D.Double(330, 345, 150, 65));

        // Legs
        g.setStroke(new BasicStroke(18, BasicStroke.CAP_ROUND,
                                    BasicStroke.JOIN_ROUND));
        g.setColor(new Color(30, 150, 90));
        g.drawLine(330, 390, 310, 445);
        g.drawLine(450, 390, 470, 445);

        // Claws
        g.setStroke(new BasicStroke(4));
        g.setColor(Color.WHITE);
        g.drawLine(300, 445, 290, 453);
        g.drawLine(310, 445, 305, 455);
        g.drawLine(470, 445, 475, 455);
    }

    private void drawHead(Graphics2D g) {
        g.setColor(new Color(45, 205, 125));
        g.fill(new Ellipse2D.Double(485, 250, 145, 110));

        // Snout
        g.fillRoundRect(575, 290, 90, 48, 25, 25);

        // Horns
        g.setColor(new Color(245, 210, 100));
        Polygon horn1 = new Polygon(
                new int[]{520, 535, 548}, new int[]{270, 220, 266}, 3);
        Polygon horn2 = new Polygon(
                new int[]{555, 570, 578}, new int[]{266, 222, 280}, 3);
        g.fillPolygon(horn1);
        g.fillPolygon(horn2);

        // Eye
        g.setColor(Color.WHITE);
        g.fillOval(555, 280, 24, 24);
        g.setColor(Color.BLACK);
        g.fillOval(566, 286, 8, 14);

        // Nostril
        g.fillOval(635, 305, 7, 7);
    }

    private void drawTail(Graphics2D g) {
        int wag = (int) (Math.sin(t * 1.8) * 25);
        g.setColor(new Color(35, 175, 105));
        g.setStroke(new BasicStroke(25, BasicStroke.CAP_ROUND,
                                    BasicStroke.JOIN_ROUND));
        g.drawLine(285, 360, 170, 330 + wag);

        Polygon tip = new Polygon(
                new int[]{160, 120, 165},
                new int[]{315 + wag, 330 + wag, 345 + wag}, 3);
        g.fillPolygon(tip);
    }

    private void drawWings(Graphics2D g) {
        double flap = Math.sin(t * 2.4) * 0.6;

        // Back wing
        Graphics2D wing = (Graphics2D) g.create();
        wing.rotate(-flap, 390, 320);
        Path2D shape = new Path2D.Double();
        shape.moveTo(390, 320);
        shape.lineTo(315, 150);
        shape.lineTo(400, 215);
        shape.lineTo(455, 115);
        shape.lineTo(465, 260);
        shape.lineTo(520, 180);
        shape.lineTo(495, 325);
        shape.closePath();

        wing.setColor(new Color(120, 70, 190, 210));
        wing.fill(shape);
        wing.setColor(new Color(210, 165, 255));
        wing.setStroke(new BasicStroke(4));
        wing.draw(shape);
        wing.dispose();
    }

    private void drawFire(Graphics2D g) {
        double pulse = 0.8 + 0.2 * Math.sin(t * 8);
        Graphics2D flame = (Graphics2D) g.create();
        flame.translate(655, 314);
        flame.scale(pulse, pulse);

        Path2D fire = new Path2D.Double();
        fire.moveTo(0, 0);
        fire.curveTo(45, -28, 65, -22, 100, -5);
        fire.curveTo(65, 10, 45, 28, 0, 10);
        fire.closePath();

        flame.setColor(new Color(255, 90, 25, 220));
        flame.fill(fire);

        Path2D innerFire = new Path2D.Double();
        innerFire.moveTo(0, 2);
        innerFire.curveTo(35, -10, 48, -6, 70, 0);
        innerFire.curveTo(45, 7, 30, 13, 0, 7);
        innerFire.closePath();

        flame.setColor(new Color(255, 220, 50));
        flame.fill(innerFire);
        flame.dispose();
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            JFrame frame = new JFrame("Animated Dragon");
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            frame.add(new AnimatedDragon());
            frame.pack();
            frame.setLocationRelativeTo(null);
            frame.setVisible(true);
        });
    }
}