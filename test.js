const items = ['Pencil', 'Notebook', 'yo-yo', 'Gum'];

function last(arr, cb) {
  cb(arr);
}

const lastItem = function(arr) {
  final = arr.pop();
  console.log(final);
  return final;
};

last(items, lastItem);
