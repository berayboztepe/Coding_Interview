package songsandmusicians;



import javax.swing.JButton;
import javax.swing.JLabel;
import javax.swing.JTextField;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Scanner;
import javax.swing.*;
import javax.swing.JFrame;
import java.awt.Color;


public class Main extends JFrame {

	public static void main(String[] args) {
		
		
		JFrame f=new JFrame("Song Quiz");  
		JLabel s = new JLabel("Question 1:\n\"Which one the owner of the song 'Moving on'?\n");
		s.setBounds(0,0, 500,30);
		f.add(s);
	    JButton b=new JButton("A-Avenged Sevenfold"); 
	    JButton b1=new JButton("B-Slipknot"); 
	    JButton b2=new JButton("C-)Five Finger Death Punch"); 
	    JButton b3=new JButton("D-)Asking Alexandra"); 
	    b.setBounds(0,30,200,40); 
	    f.add(b);  
	    b.addActionListener(new ActionListener() {

	        @Override
	        public void actionPerformed(ActionEvent e) {
	        	JLabel s11 = new JLabel("Wrong!");
	        	f.add(s11);
	        	s11.setBounds(700, 100, 750, 30);
	        	b.setBackground(Color.red);
	        	b1.setEnabled(false);
	        	b3.setEnabled(false);
	        	b2.setEnabled(false);
	        }
	    });
	    

	    b1.setBounds(0,70,200,40); 
	    f.add(b1);  
	    b1.addActionListener(new ActionListener() {

	        @Override
	        public void actionPerformed(ActionEvent e) {
	        	JLabel s12 = new JLabel("Wrong!");
	        	f.add(s12);
	        	s12.setBounds(700, 100, 750, 30);
	        	b1.setBackground(Color.red);
	        	b2.setEnabled(false);
	        	b3.setEnabled(false);
	        	b.setEnabled(false);
	        }
	    });
	    b2.setBounds(0,110,200,40); 
	    f.add(b2);  
	    b2.addActionListener(new ActionListener() {

	        @Override
	        public void actionPerformed(ActionEvent e) {
	        	JLabel s13 = new JLabel("Wrong!");
	        	f.add(s13);
	        	s13.setBounds(700, 100, 750, 30);
	        	b2.setBackground(Color.red);
	        	b1.setEnabled(false);
	        	b.setEnabled(false);
	        	b3.setEnabled(false);
	        }
	    });

	    b3.setBounds(0,150,200,40); 
	    f.add(b3);
	    b3.addActionListener(new ActionListener() {

	        @Override
	        public void actionPerformed(ActionEvent e) {
	        	JLabel s14 = new JLabel("Correct!");
	        	f.add(s14);
	        	s14.setBounds(700, 100, 750, 30);
	        	b3.setBackground(Color.green);
	        	b1.setEnabled(false);
	        	b.setEnabled(false);
	        	b2.setEnabled(false);
	        }
	    });
	    
	    
	    JLabel s1 = new JLabel("Question 2:\n\"Which one the owner of the song 'Remember Everything'?");
		s1.setBounds(0,190, 500,30);
		f.add(s1);
	    JButton b4=new JButton("A-)Five Finger Death Punch"); 
	    JButton b5=new JButton("B-Asking Alexandria"); 
	    JButton b6=new JButton("C-)Breaking Benjamin");
	    JButton b7=new JButton("D-)Avenged Sevenfold"); 
	    b4.setBounds(0,230,200,40); 
	    f.add(b4);
	    b4.addActionListener(new ActionListener() {

	        @Override
	        public void actionPerformed(ActionEvent e) {
	        	JLabel s21 = new JLabel("Correct!");
	        	f.add(s21);
	        	s21.setBounds(700, 290, 750, 30);
	        	b4.setBackground(Color.green);
	        	b5.setEnabled(false);
	        	b6.setEnabled(false);
	        	b7.setEnabled(false);
	        
	        }
	    });

	    b5.setBounds(0,270,200,40); 
	    f.add(b5);
	    b5.addActionListener(new ActionListener() {

	        @Override
	        public void actionPerformed(ActionEvent e) {
	        	JLabel s22 = new JLabel("Wrong!");
	        	f.add(s22);
	        	s22.setBounds(700, 290, 750, 30);
	        	b5.setBackground(Color.red);
	        	b6.setEnabled(false);
	        	b7.setEnabled(false);
	        	b4.setEnabled(false);
	        
	        }
	    });

	    b6.setBounds(0,310,200,40); 
	    f.add(b6); 
	    b6.addActionListener(new ActionListener() {

	        @Override
	        public void actionPerformed(ActionEvent e) {
	        	JLabel s23 = new JLabel("Wrong!");
	        	f.add(s23);
	        	s23.setBounds(700, 290, 750, 30);
	        	b6.setBackground(Color.red);
	        	b5.setEnabled(false);
	        	b7.setEnabled(false);
	        	b4.setEnabled(false);
	        }
	    });

	    b7.setBounds(0,350,200,40); 
	    f.add(b7); 
	    b7.addActionListener(new ActionListener() {

	        @Override
	        public void actionPerformed(ActionEvent e) {
	        	JLabel s24 = new JLabel("Wrong!");
	        	f.add(s24);
	        	s24.setBounds(700, 290, 750, 30);
	        	b7.setBackground(Color.red);
	        	b6.setEnabled(false);
	        	b5.setEnabled(false);
	        	b4.setEnabled(false);
	        	
	        }
	    });
	    
	    
	    JLabel s2 = new JLabel("Question 3:\n\"Which one the owner of the song 'A Little Piece of Heaven'?");
		s2.setBounds(0,390, 500,30);
		f.add(s2);
	    JButton b8=new JButton("A-)Linkin Park");
	    JButton b9=new JButton("B-Blue October"); 
	    JButton b10=new JButton("C-)Avenged Sevenfold"); 
	    JButton b11=new JButton("D-)System of a Down"); 
	    b8.setBounds(0,430,200,40); 
	    f.add(b8);
	    b8.addActionListener(new ActionListener() {

	        @Override
	        public void actionPerformed(ActionEvent e) {
	        	JLabel s31 = new JLabel("Wrong!");
	        	f.add(s31);
	        	s31.setBounds(700, 490, 750, 30);
	        	b8.setBackground(Color.red);
	        	b9.setEnabled(false);
	        	b10.setEnabled(false);
	        	b11.setEnabled(false);
	        }
	    });

	    b9.setBounds(0,470,200,40); 
	    f.add(b9); 
	    b9.addActionListener(new ActionListener() {

	        @Override
	        public void actionPerformed(ActionEvent e) {
	        	JLabel s32 = new JLabel("Wrong!");
	        	f.add(s32);
	        	s32.setBounds(700, 490, 750, 30);
	        	b9.setBackground(Color.red);
	        	b8.setEnabled(false);
	        	b10.setEnabled(false);
	        	b11.setEnabled(false);
	        }
	    });

	    b10.setBounds(0,510,200,40); 
	    f.add(b10); 
	    b10.addActionListener(new ActionListener() {

	        @Override
	        public void actionPerformed(ActionEvent e) {
	        	JLabel s33 = new JLabel("Correct!");
	        	f.add(s33);
	        	s33.setBounds(700, 490, 750, 30);
	        	b10.setBackground(Color.green);
	        	b9.setEnabled(false);
	        	b8.setEnabled(false);
	        	b11.setEnabled(false);
	        }
	    });

	    b11.setBounds(0,550,200,40); 
	    f.add(b11); 
	    b11.addActionListener(new ActionListener() {

	        @Override
	        public void actionPerformed(ActionEvent e) {
	        	JLabel s34 = new JLabel("Wrong!");
	        	f.add(s34);
	        	s34.setBounds(700, 490, 750, 30);
	        	b11.setBackground(Color.red);
	        	b9.setEnabled(false);
	        	b10.setEnabled(false);
	        	b8.setEnabled(false);
	        }
	    });
	    
	    
	    JLabel s3 = new JLabel("Last Question:\n\"Which one the owner of the song 'Snuff'?");
		s3.setBounds(0,590, 500,30);
		f.add(s3);
	    JButton b12=new JButton("A-)Nickelback");  
	    JButton b13=new JButton("B-Three Days Grace");
	    JButton b14=new JButton("C-)Pearl Jam"); 
	    JButton b15=new JButton("D-)Slipknot"); 
	    b12.setBounds(0,630,200,40); 
	    f.add(b12);  
	    b12.addActionListener(new ActionListener() {

	        @Override
	        public void actionPerformed(ActionEvent e) {
	        	JLabel s41 = new JLabel("Wrong!");
	        	f.add(s41);
	        	s41.setBounds(700, 690, 750, 30);
	        	b12.setBackground(Color.red);
	        	b13.setEnabled(false);
	        	b14.setEnabled(false);
	        	b15.setEnabled(false);
	        }
	    });
 
	    b13.setBounds(0,670,200,40); 
	    f.add(b13);  
	    b13.addActionListener(new ActionListener() {

	        @Override
	        public void actionPerformed(ActionEvent e) {
	        	JLabel s42 = new JLabel("Wrong!");
	        	f.add(s42);
	        	s42.setBounds(700, 690, 750, 30);
	        	b13.setBackground(Color.red);
	        	b12.setEnabled(false);
	        	b14.setEnabled(false);
	        	b15.setEnabled(false);
	        }
	    });

	    b14.setBounds(0,710,200,40); 
	    f.add(b14);
	    b14.addActionListener(new ActionListener() {

	        @Override
	        public void actionPerformed(ActionEvent e) {
	        	JLabel s43 = new JLabel("Wrong!");
	        	f.add(s43);
	        	s43.setBounds(700, 690, 750, 30);
	        	b14.setBackground(Color.red);
	        	b13.setEnabled(false);
	        	b12.setEnabled(false);
	        	b15.setEnabled(false);
	        }
	    });

	    b15.setBounds(0,750,200,40); 
	    f.add(b15); 
	    b15.addActionListener(new ActionListener() {

	        @Override
	        public void actionPerformed(ActionEvent e) {
	        	JLabel s44 = new JLabel("Correct!");
	        	f.add(s44);
	        	s44.setBounds(700, 690, 750, 30);
	        	b15.setBackground(Color.green);
	        	b13.setEnabled(false);
	        	b14.setEnabled(false);
	        	b12.setEnabled(false);
	        }
	    });
	    
		f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		f.setSize(1920, 1080);
		f.setLayout(null);
		f.setVisible(true);
	
		
		
	}
	
	

}
