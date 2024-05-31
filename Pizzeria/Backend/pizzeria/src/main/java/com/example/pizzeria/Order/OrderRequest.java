package com.example.pizzeria.Order;

public class OrderRequest {
	private Long userId;

	private String pizza;

	private Float price;

	public OrderRequest() {};

	public OrderRequest(Long userId, String pizza, Float price) {
		this.userId = userId;
        this.pizza = pizza;
        this.price = price;
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