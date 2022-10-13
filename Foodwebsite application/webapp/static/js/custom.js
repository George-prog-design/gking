$ (document).ready(function() {
  $ ('.increment-btn').click(function(e){
       e.preventDefault();

       var increment_value = $(this).closest('.product_data').find('.qty-input').val();
       var value = parseInt(increment_value,10);
       value = isNaN(value) ? 0 : value;
       if (value < 10)
       {
         value++;
         $(this).closest('.product_data').find('.qty-input').val(value);

       }

  });

     $ ('.decrement-btn').click(function (e) {
       e.preventDefault();

       var decrement_value = $(this).closest('.product_data').find('.qty-input').val();
       var value = parseInt(decrement_value,10);
       value = isNaN(value) ? 0 : value;
       if (value > 1)
       {
         value--;
         $(this).closest('.product_data').find('.qty-input').val(value);

       }

  });
});