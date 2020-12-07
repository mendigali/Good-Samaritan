import java.lang.Math;
import java.util.*; 
class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int operation = input.nextInt();
        int searchID = -1;
        String searchDate = "";
        if (operation == 2) {
            searchID = input.nextInt();
        }
        if (operation == 3) {
            searchDate = input.nextLine();
            searchDate = searchDate.trim();
        }
        int numberOfOrders = input.nextInt();
        Order[] orders = new Order[numberOfOrders];
        input.nextLine();
        for (int i = 0; i < numberOfOrders; i++) {
            String singleOrder = input.nextLine();
            orders[i] = new Order(singleOrder);
        }
        switch(operation) {
            case 1:
                getTotalPrice(orders);
                break;
            case 2:
                searchByID(orders, searchID);
                break;
            case 3:
                searchByDate(orders, searchDate);
                break;
            case 6:
                mostPopularSize(orders);
                break;
            case 7:
                mostPopularPizzaType(orders);
                break;
        }
    }
    public static void getTotalPrice(Order[] orders) {
        int total_price = 0;
        for (int i = 0; i < orders.length; i++) {
            total_price += orders[i].price;
        }
        System.out.println("Total price:");
        System.out.println(total_price);
    }
    public static void searchByID(Order[] orders, int ID) {
        boolean found = false;
        System.out.println("Search by ID: " + ID);
        for (int i = 0; i < orders.length; i++) {
            if (orders[i].ID == ID) {
                found = true;
                orders[i].printOrder();
            }
        }
        if (!found) {
            System.out.println("No result");
        }
    }
    public static void searchByDate(Order[] orders, String searchDate) {
        boolean found = false;
        System.out.println("Search by date: " + searchDate);
        for (int i = 0; i < orders.length; i++) {
            if (searchDate.equals(orders[i].date)) {
                found = true;
                orders[i].printOrder();
            }
        }
        if (!found) {
            System.out.println("No result");
        }
    }
    public static void mostPopularSize(Order[] orders) {
        int twenty = 0, thirty = 0, fourty = 0;
        for (int i = 0; i < orders.length; i++) {
            if (orders[i].size == 20) {
                twenty++;
            }
            if (orders[i].size == 30) {
                thirty++;
            }
            if (orders[i].size == 40) {
                fourty++;
            }
        }
        int max = Math.max(twenty, Math.max(thirty, fourty));
        System.out.println("Most popular size:");
        if (twenty == max) {
            System.out.println("20");
        }
        if (thirty == max) {
            System.out.println("30");
        }
        if (fourty == max) {
            System.out.println("40");
        }
    }
    public static void mostPopularPizzaType(Order[] orders) {
        HashMap<String, Integer> map = new HashMap<String, Integer>();
        int max = 0;
        for (int i = 0; i < orders.length; i++) {
            String combination = "";
            combination += (orders[i].topping1 ? "1" : "0"); // cheese
            combination += (orders[i].topping2 ? "1" : "0"); // meet
            combination += (orders[i].topping3 ? "1" : "0"); // sausage
            combination += (orders[i].topping4 ? "1" : "0"); // vegetables

            boolean combinationExists = false;
            for (Map.Entry<String, Integer> currentCombination : map.entrySet()) {
                if (combination.equals(currentCombination.getKey())) {
                   combinationExists = true;
                }
            }
            if (combinationExists) {
                int repeated = map.get(combination)+1;
                max = Math.max(max, repeated);
                map.replace(combination, repeated);
            }
            else {
                max = Math.max(max, 1);
                map.put(combination, 1);
            }
        }
        System.out.println("Most popular pizza type(s):");
        for (Map.Entry<String, Integer> currentCombination : map.entrySet()) {
            if (currentCombination.getValue() == max) {
                String combination = currentCombination.getKey(); // 1011
                String result = "";
                if (combination.charAt(0) == '1') { // Cheese
                    result += "Cheese";
                }
                if (combination.charAt(1) == '1') { // Meet
                    if (result.length() > 0) {
                        result += "+";
                    }
                    result += "Meet";
                }
                if (combination.charAt(2) == '1') { // Sausage
                    if (result.length() > 0) {
                        result += "+";
                    }
                    result += "Sausage";
                }
                if (combination.charAt(3) == '1') { // Vegetables
                    if (result.length() > 0) {
                        result += "+";
                    }
                    result += "Vegetables";
                }
                System.out.println(result);
            }
        }
    }
}
class Order {
    int ID;
    String date;
    String time;
    int price;
    boolean isBirthday;
    int size;
    boolean topping1; // cheese
    boolean topping2; // meet
    boolean topping3; // sausage
    boolean topping4; // vegetables
    public Order(String currentOrder) {
        String[] splitOrder = currentOrder.trim().split("\\s+");
        this.ID = Integer.parseInt(splitOrder[0]);
        this.date = splitOrder[1].trim();
        this.time = splitOrder[2].trim();
        this.price = Integer.parseInt(splitOrder[3]);
        this.isBirthday = splitOrder[4].equals("Yes") ? true : false;
        this.size = Integer.parseInt(splitOrder[5]);
        this.topping1 = splitOrder[6].equals("Yes") ? true : false;
        this.topping2 = splitOrder[7].equals("Yes") ? true : false;
        this.topping3 = splitOrder[8].equals("Yes") ? true : false;
        this.topping4 = splitOrder[9].equals("Yes") ? true : false;
    }
    public void printOrder() {
        System.out.println(this.ID + " " + this.date + " " + this.time + " " + this.price + " " + (this.isBirthday ? "Yes" : "No") + " " + this.size + " " + (this.topping1 ? "Yes" : "No") + " " + (this.topping2 ? "Yes" : "No") + " " + (this.topping3 ? "Yes" : "No") + " " + (this.topping4 ? "Yes" : "No") + " ");
    }
}