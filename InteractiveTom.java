import java.awt.*;
import java.awt.event.*;
import java.awt.geom.*;
import javax.swing.*;

public class InteractiveTom extends JPanel {
    private double tomX = 400, tomY = 340;
    private double targetX = 400, targetY = 340;
    private double time = 0;
    private long lastClickTime = 0;
    private String message = "Move the mouse to guide Tom. Click him to pet him!";
    private final Timer timer;

    public InteractiveTom() {
        setPreferredSize(new Dimension(800, 600));
        setBackground(new Color(190, 225, 245));

        addMouseMotionListener(new MouseMotionAdapter() {
            @Override
            public void mouseMoved(MouseEvent e) {
                targetX = clamp(e.getX(), 110, getWidth() - 110);
                targetY = clamp(e.getY() + 80, 220, getHeight() - 170);
            }
        });

        addMouseListener(new MouseAdapter() {
            @Override
            public void mouseClicked(MouseEvent e) {
                double dx = e.getX() - tomX;
                double dy = e.getY() - (tomY - 35);
                if (Math.hypot(dx, dy) < 110) {
                    message = "Tom purrs happily!  Meow!";
                    lastClickTime = System.currentTimeMillis();
                } else {
                    message = "Click Tom to pet him!";
                }
            }
        });

        addKeyListener(new KeyAdapter() {
            @Override
            public void keyPressed(KeyEvent e) {
                if (e.getKeyCode() == KeyEvent.VK_SPACE) {
                    message = "Tom says: Meow!";
                    lastClickTime = System.currentTimeMillis();
                }
            }
        });
        setFocusable(true);

        timer = new Timer(16, e -> {
            time += 0.05;
            tomX += (targetX - tomX) * 0.04;
            tomY += (targetY - tomY) * 0.04;

            if (System.currentTimeMillis() - lastClickTime > 2200
                    && (message.startsWith("Tom purrs") || message.equals("Tom says: Meow!"))) {
                message = "Move the mouse to guide Tom. Click him to pet him!";
            }
            repaint();
        });
        timer.start();
    }

    private static double clamp(double value, double min, double max) {
        return Math.max(min, Math.min(max, value));
    }

    @Override
    protected void paintComponent(Graphics graphics) {
        super.paintComponent(graphics);
        Graphics2D g = (Graphics2D) graphics.create();
        g.setRenderingHint(RenderingHints.KEY_ANTIALIASING,
                           RenderingHints.VALUE_ANTIALIAS_ON);

        // Background floor
        g.setColor(new Color(145, 195, 215));
        g.fillRect(0, getHeight() - 65, getWidth(), 65);

        double bob = Math.sin(time * 2) * 4;
        double x = tomX;
        double y = tomY + bob;

        // Ground shadow
        g.setColor(new Color(100, 145, 165, 100));
        g.fillOval((int) x - 90, (int) y + 135, 180, 25);

        drawTail(g, x, y);
        drawBody(g, x, y);
        drawHead(g, x, y);
        drawMessage(g);

        g.dispose();
    }

    private void drawTail(Graphics2D g, double x, double y) {
        double wag = Math.sin(time * 3) * 20;
        g.setColor(new Color(125, 130, 140));
        g.setStroke(new BasicStroke(16, BasicStroke.CAP_ROUND, BasicStroke.JOIN_ROUND));
        g.draw(new QuadCurve2D.Double(x - 65, y + 85,
                x - 140, y + 45 + wag, x - 115, y + 5 + wag));
    }

    private void drawBody(Graphics2D g, double x, double y) {
        g.setColor(new Color(130, 135, 145));
        g.fillOval((int) x - 80, (int) y + 20, 160, 130);

        // Belly
        g.setColor(new Color(215, 215, 220));
        g.fillOval((int) x - 45, (int) y + 48, 90, 85);

        // Paws
        g.setColor(new Color(125, 130, 140));
        g.fillOval((int) x - 65, (int) y + 125, 58, 28);
        g.fillOval((int) x + 7, (int) y + 125, 58, 28);
    }

    private void drawHead(Graphics2D g, double x, double y) {
        // Ears
        g.setColor(new Color(125, 130, 140));
        Polygon leftEar = new Polygon(
                new int[]{(int) x - 65, (int) x - 58, (int) x - 18},
                new int[]{(int) y - 65, (int) y - 145, (int) y - 90}, 3);
        Polygon rightEar = new Polygon(
                new int[]{(int) x + 18, (int) x + 58, (int) x + 65},
                new int[]{(int) y - 90, (int) y - 145, (int) y - 65}, 3);
        g.fillPolygon(leftEar);
        g.fillPolygon(rightEar);

        // Inner ears
        g.setColor(new Color(245, 155, 170));
        g.fillPolygon(new Polygon(
                new int[]{(int) x - 53, (int) x - 49, (int) x - 29},
                new int[]{(int) y - 92, (int) y - 126, (int) y - 96}, 3));
        g.fillPolygon(new Polygon(
                new int[]{(int) x + 29, (int) x + 49, (int) x + 53},
                new int[]{(int) y - 96, (int) y - 126, (int) y - 92}, 3));

        // Head
        g.setColor(new Color(135, 140, 150));
        g.fillOval((int) x - 75, (int) y - 105, 150, 145);

        // Eyes follow the mouse
        Point mouse = getMousePosition();
        double lookX = 0, lookY = 0;
        if (mouse != null) {
            double dx = mouse.x - x;
            double dy = mouse.y - (y - 45);
            double length = Math.max(1, Math.hypot(dx, dy));
            lookX = dx / length * 5;
            lookY = dy / length * 4;
        }

        boolean blink = (System.currentTimeMillis() % 3400) < 140;
        if (blink) {
            g.setColor(new Color(55, 60, 70));
            g.setStroke(new BasicStroke(4));
            g.drawLine((int) x - 43, (int) y - 43, (int) x - 15, (int) y - 43);
            g.drawLine((int) x + 15, (int) y - 43, (int) x + 43, (int) y - 43);
        } else {
            g.setColor(Color.WHITE);
            g.fillOval((int) x - 47, (int) y - 68, 38, 50);
            g.fillOval((int) x + 9, (int) y - 68, 38, 50);

            g.setColor(new Color(70, 150, 225));
            g.fillOval((int) (x - 33 + lookX), (int) (y - 52 + lookY), 17, 26);
            g.fillOval((int) (x + 19 + lookX), (int) (y - 52 + lookY), 17, 26);

            g.setColor(Color.BLACK);
            g.fillOval((int) (x - 29 + lookX), (int) (y - 48 + lookY), 8, 17);
            g.fillOval((int) (x + 23 + lookX), (int) (y - 48 + lookY), 8, 17);
        }

        // Muzzle, nose, and mouth
        g.setColor(new Color(230, 225, 220));
        g.fillOval((int) x - 38, (int) y - 12, 38, 28);
        g.fillOval((int) x, (int) y - 12, 38, 28);

        g.setColor(new Color(245, 155, 170));
        g.fillPolygon(new Polygon(
                new int[]{(int) x - 9, (int) x + 9, (int) x},
                new int[]{(int) y - 5, (int) y - 5, (int) y + 6}, 3));

        g.setColor(new Color(55, 60, 70));
        g.setStroke(new BasicStroke(2));
        g.drawArc((int) x - 13, (int) y + 1, 13, 13, 180, 180);
        g.drawArc((int) x, (int) y + 1, 13, 13, 180, 180);

        // Whiskers
        g.setColor(Color.WHITE);
        for (int i = 0; i < 3; i++) {
            int offset = i * 9;
            g.drawLine((int) x - 33, (int) y + offset,
                       (int) x - 82, (int) y + offset - 10 + i * 7);
            g.drawLine((int) x + 33, (int) y + offset,
                       (int) x + 82, (int) y + offset - 10 + i * 7);
        }
    }

    private void drawMessage(Graphics2D g) {
        g.setFont(new Font("SansSerif", Font.BOLD, 20));
        g.setColor(new Color(45, 55, 65));
        g.drawString(message, 20, 35);

        g.setFont(new Font("SansSerif", Font.PLAIN, 15));
        g.drawString("Move mouse: Tom follows  |  Click Tom: pet  |  Space: meow",
                     20, getHeight() - 20);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            JFrame frame = new JFrame("Interactive Tom");
            InteractiveTom panel = new InteractiveTom();
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            frame.add(panel);
            frame.pack();
            frame.setLocationRelativeTo(null);
            frame.setVisible(true);
            panel.requestFocusInWindow();
        });
    }
}
