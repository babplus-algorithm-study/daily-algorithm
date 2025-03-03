```
#include <iostream>
#include <vector>
using namespace std;

struct Node {
    int value;
    Node* left;
    Node* right;
    
    Node(int val) : value(val), left(nullptr), right(nullptr) {}
};

void insert(Node*& root, int val) {
    if (root == nullptr) {
        root = new Node(val);
        return;
    }
    if (val < root->value) {
        insert(root->left, val);
    } else {
        insert(root->right, val);
    }
}

void postOrder(Node* root) {
    if (root == nullptr) return;
    postOrder(root->left);
    postOrder(root->right);
    cout << root->value << '\n';
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    
    Node* root = nullptr;
    int num;
    while (cin >> num) {
        insert(root, num);  // BST 구성
    }
    
    postOrder(root);  // 후위 순회 수행

    return 0;
}

```
