// package com.example.pizzeria.Menu;

// import jakarta.persistence.*;

// @Entity
// @Table(name = "menu")
// public class Menu {
//     @Id
// 	@GeneratedValue(strategy =  GenerationType.IDENTITY)
// 	private Long id;
	
// 	@Column(name = "name")
// 	private String name;
	
// 	@Column(name = "price")
// 	private Float price;

// 	public Menu() {};

// 	public Menu(String name, Float price) {
//         this.name = name;
//         this.price = price;
//     }
// 	public Menu(Long id, String name, Float price) {
// 		this.id = id;
//         this.name = name;
//         this.price = price;
//     }
// 	public long getId() {
// 		return id;
// 	}
// 	public void setId(long id) {
// 		this.id = id;
// 	}
// 	public String getName() {
// 		return name;
// 	}
// 	public void setName(String name) {
// 		this.name = name;
// 	}
//     public Float getPrice() {
// 		return price;
// 	}
// 	public void setPrice(Float price) {
// 		this.price = price;
// 	}
// }
