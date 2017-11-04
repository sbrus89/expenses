def sum_list(expense_list):
  total = 0.0
  for expense in expense_list:
    total = total + expense['amount']
  
  return total
  
  