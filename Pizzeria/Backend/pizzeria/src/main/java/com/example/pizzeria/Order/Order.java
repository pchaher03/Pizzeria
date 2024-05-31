package com.example.pizzeria.Order;

import java.io.Serializable;

import jakarta.persistence.*;

@Entity
@Table(name = "orders")
public class Order implements Serializable {
	@Id
	@GeneratedValue(strategy =  GenerationType.IDENTITY)
	private Long id;

	@Column(name = "user_id")
	private Long userId;

	@Column(name = "pizza")
	private String pizza;

	@Column(name = "price")
	private Float price;

	public Order() {};

	public Order(Long userId, String pizza, Float price) {
		this.userId = userId;
        this.pizza = pizza;
        this.price = price;
    }

	public Order(Long id, Long userId, String pizza, Float price) {
		this.id = id;
		this.userId = userId;
        this.pizza = pizza;
        this.price = price;
    }

	public Long getId() {
		return id;
	}

	public void setId(Long id) {
		this.id = id;
	}

	public Long getUserId() {
		return userId;
	}

	public void setUserId(Long userId) {
		this.userId = userId;
	}

	public String getPizza() {
		return pizza;
	}

	public void setPizza(String pizza) {
		this.pizza = pizza;
	}

	public Float getPrice() {
		return price;
	}

	public void setPrice(Float price) {
		this.price = price;
	}
}