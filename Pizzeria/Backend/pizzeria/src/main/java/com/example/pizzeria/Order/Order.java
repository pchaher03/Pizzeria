package com.example.pizzeria.Order;

import java.util.List;

import jakarta.persistence.*;

@Entity
@Table(name = "orders")
public class Order {
    @Id
	@GeneratedValue(strategy =  GenerationType.IDENTITY)
	private Long id;
	
	@Column(name = "user_id")
	private Long userId;

	@Column(name = "direction")
	private String direction;

	@Column(name = "items")
	private List<Long> items;

	@Column(name = "total")
	private float total;

	public Order() {};

	public Order(Long userId, String direction, List<Long> items, Float total) {
		this.userId = userId;
        this.direction = direction;
        this.items = items;
		this.total = total;
    }

	public Order(Long id, Long userId, String direction, List<Long> items, Float total) {
		this.id = id;
		this.userId = userId;
        this.direction = direction;
        this.items = items;
		this.total = total;
    }

	public long getId() {
		return id;
	}

	public void setId(long id) {
		this.id = id;
	}

	public long getUserId() {
		return userId;
	}

	public void setUserId(long userId) {
		this.userId = userId;
	}

	public String getDirection() {
		return direction;
	}

	public void setDirection(String direction) {
		this.direction = direction;
	}

	public List<Long> getItems() {
		return items;
	}

	public void setItems(List<Long> items) {
		this.items = items;
	}

	public Float getTotal() {
		return total;
	}
	
	public void setTotal(Float total) {
		this.total = total;
	}
}
